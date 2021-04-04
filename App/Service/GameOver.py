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
    
