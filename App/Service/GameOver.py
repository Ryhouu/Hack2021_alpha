from Frame import Player, Bottle, Maze

def get_winner_HI(human : Player, robot : Player):
    # return the winner when comparing HI
    HI_h = human.getHumanIndex()
    HI_r = robot.getHumanIndex()

    return human if HI_h > HI_r else robot

def check_collision(human : Player, robot : Player) :
    return human.locX == robot.locX and human.locY == robot.locY

def check_exit(maze : Maze, player : Player) :
    if maze.end == None :
        return False
    return player.locX == maze.end.locX and player.locY == maze.end.locY

def check_bomb(maze : Maze, player : Player) :
    x, y = player.locX, player.locY
    entry = maze.mat[x][y]
    if entry.bottle is not None:
        resp = entry.bottle.isBomb()
        if resp :
            maze.mat[x][y].setColor("yellow")
            return True
    return False



def check(maze, human : Player, robot : Player) :
    winner, msg = None, ""
    
    if check_collision(human, robot) or \
        check_exit(maze, human) or check_exit(maze, robot):
        winner = get_winner_HI(human, robot)
    
    if check_bomb(maze, human) :
        print ("BOMB!")
        winner = robot
    elif check_bomb(maze, robot) :
        print ("BOMB!")
        winner = human
    
    if winner is not None :
        msg = f"{winner.identity} wins the game"
    return winner is not None, msg

    

