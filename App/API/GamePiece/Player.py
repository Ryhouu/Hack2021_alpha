# from ABC import abstract

class Player (object) :
    identity = None
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

