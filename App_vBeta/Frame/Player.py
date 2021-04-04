import time, math, random
from Frame.Maze import Maze
from _config import MAZE, ROBOT, HUMAN
from Frame.Component import Component

class Player (Component) :
    HI = None
    identity = None
    vision = None
    speed = None
    memory = None
    tim = time.time()

    locX = -1
    locY = -1

    def __init__(self, id : str, v : int, s : int, m : int) -> None:
        super().__init__()
        self.identity = id
        self.vision = v
        self.speed = s
        self.memory = m
    
    def getHumanIndex (self) -> int :
        return self.memory - self.vision - self.speed
    
    def pick_bottle (self, bottle) :
        if bottle is not None:
            if bottle.isMemory() :
                if self.memory != 5 :
                    self.memory += 1
                    self.vision -= 1
                    self.speed -= 1

    def move (self, nxtX : int, nxtY : int) :
        self.locX = nxtX
        self.locY = nxtY
    
    def tp (self, maze: Maze):
        ## player will be transported to
        cham_index = random.randint(0, len(maze.chambers)-1)
        ## the coordination of the destination chamber
        dest_chambers_X = maze.chambers[cham_index][0]
        dest_chambers_Y = maze.chambers[cham_index][1]
        if maze.mat[self.locX][self.locY].isChamber():
            dest_bottle = maze.mat[dest_chambers_X][dest_chambers_Y].bottle
            maze.mat[self.locX][self.locY].setBottle(dest_bottle)
            self.locX = dest_chambers_X
            self.locY = dest_chambers_Y
    
    def moveDir (self, maze : Maze, dir : str) :
        if time.time() - self.tim > 0.5/self.speed :
            self.tim = time.time()
            Delta = {
                "W" : (-1, 0),
                "E" : (1, 0),
                "N" : (0, -1),
                "S" : (0, 1)
            }
            if dir == 'tp' :
                self.tp(maze)
                return
            else:
                nxtX, nxtY = self.locX + Delta[dir][0], self.locY + Delta[dir][1]

            if not maze.mat[nxtX][nxtY].isWall() :
                self.move(nxtX, nxtY)
                x, y = self.locX, self.locY
                entry = maze.mat[x][y]
                self.pick_bottle(entry.bottle)

        

    def getLocation (self) -> tuple :
        return (self.locX, self.locY)
    

    
