# from ABC import abstract
from config import Robot, Human

class Player (object) :
    HI = None
    vision = None
    speed = None
    memory = None

    def __init__(self) -> None:
        super().__init__()

    # @abstractMethod
    def move (self) :
        pass

    def pick_bottle (self) :
        pass


class Robot (Player) :
    def __init__(self) -> None:
        self.vision = 2
        self.speed = robot_default_speed
        self.memory
        super().__init__()


print (Robot.default_speed)