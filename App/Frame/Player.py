
from _config import Robot, Human
from Component import Component

class Player (Component) :
    HI = None
    identity = None
    vision = None
    speed = None
    memory = None

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

    def move (self, nxtX, nxtY) :
        pass

    def pick_bottle (self, bottle) :
        pass

    def getLocation (self) -> tuple :
        return (self.locX, self.locY)
    




def create_new_robot () :
    robot = Player (
        Robot.default_identity,
        Robot.default_vision,
        Robot.default.speed,
        Robot.default_memory)
    
