from _config import BOTTLE
from Component import Component
import random

class Bottle(Component) :
    attr = ""

    def __init__(self, a) -> None:
        super().__init__()
        self.attr = a

    def getAttr(self) -> str :
        return self.attr


class RandBottle (object) :
    def __init__(self) -> None:
        super().__init__()

    def rand(self) :
        x = random.randint(0, 1)
        return Bottle (str(x))


b = RandBottle().rand()
print (b.attr)