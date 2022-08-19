from Session.cmu_112_graphics import *
from _config import CANVAS, MAZE, BOTTLE, HUMAN, ROBOT
from Frame.Maze import Maze
from Frame.Player import Player
from Service import EnterChamber
from Service import GameOver


rawMat = MAZE.default_mat

def getCord(app, i, j) :
    # return the cord of the top-left corner of the entry at [i, j]
    return i * app.unit, j * app.unit

def appStarted(app):
    app.maze = Maze(MAZE.default_mat)
    app.unit = (CANVAS.width - 200) // MAZE.width
    app.pad = 3

    app.human = Player(
        HUMAN.default_identity,
        HUMAN.default_vision,
        HUMAN.default_speed,
        HUMAN.default_memory)

    app.human.move(1, 1)
    
    app.robot = Player(
        ROBOT.default_identity,
        ROBOT.default_vision,
        ROBOT.default_speed,
        ROBOT.default_memory)
    
    app.robot.move(18, 18)
    
    app.msg = "is huntings"
    app.gameover = False
    app.winner = None
    app.hunter = 'human'


def drawMaze(app, canvas):
    for i in range(MAZE.width):
        for j in range(MAZE.height):
            x, y = getCord(app, i, j)
            canvas.create_rectangle(
                x, y, x + app.unit, y + app.unit, fill = app.maze.mat[i][j].color)

    x, y = getCord(app, app.human.locX, app.human.locY)
    if not app.maze.mat[app.human.locX][app.human.locY].isChamber():
        canvas.create_oval(
            x + app.pad, y + app.pad, 
            x + app.unit - app.pad, y + app.unit - app.pad, fill = 'blue')
        canvas.create_text(x + app.unit/2, y + app.unit/2, text = 'H', font = 'bold')
    
    x, y = getCord(app, app.robot.locX, app.robot.locY)
    if not app.maze.mat[app.robot.locX][app.robot.locY].isChamber():
        canvas.create_oval(
            x + app.pad, y + app.pad, 
            x + app.unit - app.pad, y + app.unit - app.pad, fill = 'red')
        canvas.create_text(x + app.unit/2, y + app.unit/2, text = 'R', font = 'bold')


def keyPressed(app, event):
    if app.gameover :
        # restart?
        return
    if event.key in CANVAS.DIR_human.keys() :
        # if up_chamber (app.maze,app.human):
        #     if event.key == "up" :
        #         msg = ""
        #         x = get_player_position(app.human)[0]
        #         y = get_player_position(app.human)[1]
        #         if app.maze.mat[x][y+1].isBomb():
        #             msg = "There is Bomb inside!"
        #         else:
        #             msg = "There is no Bomb inside."
        # elif left_chamber (app.maze, app.human):
        #     if event.key == "left" :
        #         msg = ""
        #         x = get_player_position(app.human)[0]
        #         y = get_player_position(app.human)[1]
        #         if app.maze.mat[x-1][y].isBomb():
        #             msg = "There is Bomb inside!"
        #         else :
        #             msg = "There is no Bomb inside." 
        # elif right_chamber (app.maze, app.human):
        #     if event.key == "right" :
        #         msg = ""
        #         x = get_player_position(app.human)[0]
        #         y = get_player_position(app.human)[1]
        #         if app.maze.mat[x+1][y].isBomb():
        #             msg = "There is Bomb inside!"
        #         else :
        #             msg = "There is no Bomb inside." 
        # elif down_chamber (app.maze, app.human):
        #     if event.key == "down" :
        #         msg = ""
        #         x = get_player_position(app.human)[0]
        #         y = get_player_position(app.human)[1]
        #         if app.maze.mat[x][y-1].isBomb():
        #             msg = "There is Bomb inside!"
        #         else :
        #             msg = "There is no Bomb inside." 

        # else :
        app.human.moveDir(app.maze, CANVAS.DIR_human[event.key])
    elif event.key in CANVAS.DIR_robot.keys() :
        # if up_chamber (app.maze,app.robot):
        #     if event.key == "w" :
        #         msg = ""
        #         x = get_player_position(app.robot)[0]
        #         y = get_player_position(app.robot)[1]
        #         if app.maze.mat[x][y+1].isBomb():
        #             msg = "There is Bomb inside!"
        #         else :
        #             msg = "There is no Bomb inside."
        # elif left_chamber (app.maze, app.robot):
        #     if event.key == "a" :
        #         msg = ""
        #         x = get_player_position(app.robot)[0]
        #         y = get_player_position(app.robot)[1]
        #         if app.maze.mat[x-1][y].isBomb():
        #             msg = "There is Bomb inside!"
        #         else :
        #             msg = "There is no Bomb inside." 
        # elif right_chamber (app.maze, app.robot):
        #     if event.key == "d" :
        #         msg = ""
        #         x = get_player_position(app.robot)[0]
        #         y = get_player_position(app.robot)[1]
        #         if app.maze.mat[x+1][y].isBomb():
        #             msg = "There is Bomb inside!"
        #         else :
        #             msg = "There is no Bomb inside." 
        # elif down_chamber (app.maze, app.robot):
        #     if event.key == "s" :
        #         msg = ""
        #         x = get_player_position(app.robot)[0]
        #         y = get_player_position(app.robot)[1]
        #         if app.maze.mat[x][y-1].isBomb():
        #             msg = "There is Bomb inside!"
        #         else :
        #             msg = "There is no Bomb inside." 

        
        app.robot.moveDir(app.maze, CANVAS.DIR_robot[event.key])
    
    resp, msg = GameOver.check(app, app.maze, app.human, app.robot) 
    if resp :
        print ("game over")
        app.gameover = True
        app.msg = msg
    


# TODO: fix this
def displayMsg(app, canvas) :
    canvas.create_oval(650, 80, 674, 104, fill = 'blue')
    canvas.create_text(680, 100, text = "memory: " + str(app.human.memory), 
        anchor = "sw", font="Times 20")
    canvas.create_text(680, 120, text = "vision: " + str(app.human.vision), 
        anchor = "sw", font="Times 20")
    canvas.create_text(680, 140, text = "speed: " + str(app.human.speed), 
        anchor = "sw", font="Times 20")
    canvas.create_oval(650, 180, 674, 204, fill = 'red')
    canvas.create_text(680, 200, text = "memory: " + str(app.robot.memory), 
        anchor = "sw", font="Times 20")
    canvas.create_text(680, 220, text = "vision: " + str(app.robot.vision), 
        anchor = "sw", font="Times 20")
    canvas.create_text(680, 240, text = "speed: " + str(app.robot.speed), 
        anchor = "sw", font="Times 20")
    # if app.winner != None :
    if app.hunter == 'human' :
        canvas.create_oval(675, 350, 725, 400, fill='blue')
    else :
        canvas.create_oval(675, 350, 725, 400, fill='red')
    canvas.create_text(700, 420, text = app.msg,
        font="Times 25 bold")


def drawMsgBox(app, canvas):
    pass
    
    
def redrawAll(app, canvas):
    drawMaze(app, canvas)
    displayMsg(app, canvas)
    
def run():
    runApp(width=CANVAS.width, height=CANVAS.height)