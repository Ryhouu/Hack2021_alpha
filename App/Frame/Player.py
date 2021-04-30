
from Frame.Maze import Maze
from _config import MAZE, ROBOT, HUMAN, CANVAS
from Frame.Component import Component
import random, time

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
            
            if dir == 'tp' :
                self.tp(maze)
                return True
            else :
                delta = CANVAS.DIR["delta"]
                nxtX, nxtY = self.locX + delta[dir][0], self.locY + delta[dir][1]
            
            if not maze.isValidEntry(nxtX, nxtY) :
                return False

            if not maze.mat[nxtX][nxtY].isWall() :
                self.move(nxtX, nxtY)
                return True
                # self.pick_bottle(maze.mat[nxtX][nxtY].bottle)
        

    def getLocation (self) -> tuple :
        return (self.locX, self.locY)
    

    
