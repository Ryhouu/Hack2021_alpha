main
def compare_human_index (human, robot):
    ##define two local variables to store the human index of the human&robot
    human_index=human.memory-human.speed-human.vision
    robot_index=robot.memory-robot.speed-robot.vision
    #compare the humanity index between the human and the robot
    if (human_index>robot_index):
        print("player1 wins the game")
    else:
        print("player2 wins the game")

def compare_location (human, robot):
    if (human.x1==robot.x1) and (robot.x2==robot.x2):
        return True
    else: 
        return False

def exit_or_not (player, graph):
    if (player.x1==graph.exit.x1) and (player.x2==graph.exit.x2):
        return True
    else:
        return False

class GameOver():

    def winner(self, graph, human, robot):
        ## if the human meets the robot, compare their human index
        if compare_location (human, robot):
            compare_human_index(human, robot)

         ## if a player gets out out of the maze
       """  elif exit_or_not (human, graph) or exit_or_not (robot,graph):
            compare_human_index (human,robot) """
        ##if there is no winner,return None
        else:
            return None


    def bomb (self,graph,player):

        ## if a player meets the bomb, the player loses the game
        tmpCell= graph.mat[x][y]
        if tmpCell.bottle is bottle.bomb :
            print("%s, lose the game", player.identity)
        else：
            return None

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

    

main
main
