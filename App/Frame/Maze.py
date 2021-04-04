from _config import MAZE
from Component import Component

class Entry(Component) :
    attr = "" # "path" / "wall" / "chamber"
    bottle = None
    color = None # media

    def __init__(self, a) -> None:
        super().__init__()
        self.attr = a
    
    def setBottle (self, bottle) :
        self.bottle = bottle

    def isChamber(self, tp) :
        return self.attr == "chamber"

    def setColor(self, c) : 
        self.color = c
    
    def __str__(self) -> str:
        return self.attr


class Maze(Component) :
    attr = ""

    mat = [[Entry(None) for i in range (MAZE.height)] for j in range (MAZE.width)]
    
    def __init__(self) -> None:
        super().__init__()

    def tester (self) :
        self.mat[0][0] = Entry("path")
        self.mat[0][1] = Entry("wall")
        print (self.mat[0][0], self.mat[0][1])

# m = Maze()
# m.tester()
