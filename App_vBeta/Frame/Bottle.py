from _config import BOTTLE
from Frame.Component import Component
import random

class Bottle(Component) :
    attr = ""

    def __init__(self, a) -> None:
        super().__init__()
        self.attr = a

    def getAttr(self) -> str :
        return self.attr
    
    def isMemory(self):
        return self.attr == "memory"
    
    def isBomb(self):
        return self.attr == "bomb"
    

class RandBottle (object) :
    def __init__(self) -> None:
        super().__init__()

    def rand(self) :
        x = random.randint(1, 100)
        a = "memory" if x > BOTTLE.pBomb else "bomb" 
        return Bottle (a)
