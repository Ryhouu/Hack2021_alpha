from _config import BOTTLE, MAZE
from Frame.Component import Component
from Frame.Bottle import Bottle, RandBottle
import random

class Entry(Component) :
    attr = "" # "path" / "wall" / "chamber"
    bottle = None
    color = None # media

    def __init__(self, a) -> None:
        super().__init__()
        self.attr = a
    
    def setBottle (self, bottle) :
        self.bottle = bottle

    def isWall(self) :
        return self.attr == "wall"

    def isChamber(self) :
        return self.attr == "chamber"

    def setColor(self, c) : 
        self.color = c
    
    def __str__(self) -> str:
        return self.attr
    
    def rm_chamber(self) :
        if self.isChamber() :
            self.attr = "wall"
            self.setColor(MAZE.wall_color)
            self.bottle = None
    
    def add_chamber(self) :
        if self.isWall() :
            self.attr = "chamber"
            self.setColor(MAZE.chamber_color)
            self.setBottle(RandBottle().rand())


class Maze(Component) :
    attr = ""

    mat = [[Entry(None) for i in range (MAZE.height)] for j in range (MAZE.width)]
    end = None
    chambers = []
    
    def __init__(self, rawMat) -> None:
        super().__init__()

        for i in range (len(rawMat)) :
            for j in range (len(rawMat[0])) :
                if rawMat[i][j] == 0 :
                    self.mat[i][j] = Entry ("wall")
                    self.mat[i][j].setColor(MAZE.wall_color)
                    if i >= 1 and i <= MAZE.width - 2 and j >= 1 and j <= MAZE.width - 2 :
                        p = random.randint(1, 100)
                        if p <= BOTTLE.pChamber :
                            self.mat[i][j].add_chamber()
                            self.chambers.append((i, j))
                elif rawMat[i][j] == 1 :
                    self.mat[i][j] = Entry ("path")
                    self.mat[i][j].setColor(MAZE.path_color)

    def tester (self) :
        self.mat[0][0] = Entry("path")
        self.mat[0][1] = Entry("wall")
        print (self.mat[0][0], self.mat[0][1])

    
