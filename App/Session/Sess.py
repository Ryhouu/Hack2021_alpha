from Session.cmu_112_graphics import *
from _config import CANVAS, MAZE, BOTTLE, HUMAN, ROBOT
from Frame.Maze import Maze
from Frame.Player import Player
from Service import GameOver, ChamberChecker, BottlePicker


def getCord(app, i, j) :
    # return the cord of the top-left corner of the entry at [i, j]
    return i * app.mazeUnit, j * app.mazeUnit

def appStarted(app):
    app.maze = Maze(MAZE.default_mat)
    app.mazeUnit = CANVAS.maze_width // MAZE.width
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
    
    app.msg = ""
    app.gameover = False
    app.winner = None

    app.queryMode = False
    app.query = ""
    app.queryAns = None

    app.memUpdate = False


def drawMaze(app, canvas):
    for i in range(MAZE.width):
        for j in range(MAZE.height):
            x, y = getCord(app, i, j)
            canvas.create_rectangle(
                x, y, x + app.mazeUnit, y + app.mazeUnit, fill=app.maze.mat[i][j].color, outline="#CDC9C9", width=1)

    x, y = getCord(app, app.human.locX, app.human.locY)
    canvas.create_oval(
        x + app.pad, y + app.pad, 
        x + app.mazeUnit - app.pad, y + app.mazeUnit - app.pad, fill=CANVAS.human_color, outline=CANVAS.human_color)
    
    x, y = getCord(app, app.robot.locX, app.robot.locY)
    canvas.create_oval(
        x + app.pad, y + app.pad, 
        x + app.mazeUnit - app.pad, y + app.mazeUnit - app.pad, fill=CANVAS.robot_color, outline=CANVAS.robot_color)


# TODO : query for enter the chamber or not
def chamberQuery(app, maze, player, dir) :
    return True
    
    # x, y = ChamberChecker.getLoc(maze, player, dir)
    # if ChamberChecker.isChamber(maze, x, y) :
    #     if ChamberChecker.isBomb(maze, x, y) :
    #         app.msg = "There is BOMB inside!! Do you want to continue?"
    #     app.queryMode = True
    #     app.query = "bomb_query"
    
    # resp, msg = ChamberChecker.run(maze, player, dir)
    # if resp :
    #     if msg == "bomb" :
        
    #         app.msg = "There is BOMB inside!!"
    #         return False
    #     else :
    #         app.msg = "There is no BOMB inside LoL"
    # return True


def keyPressed(app, event):
    if app.gameover :
        # restart?
        return

    # if app.queryMode :
    #     quitQuery = True
    #     if event.key == "y" or event.key == "Y" :
    #         app.queryAns = "Y"
    #         if app.query == "bomb_query"
    #     elif event.key == "n" or event.key == "N" :
    #         app.queryAns = "N"
    #     else :
    #         quitQuery = False
    #     app.queryMode = not quitQuery

    if event.key in CANVAS.DIR["human"].keys() :
        dir = CANVAS.DIR["human"][event.key]
        if chamberQuery(app, app.maze, app.human, dir) :
            app.human.moveDir(app.maze, dir)
            BottlePicker.run(app.maze.mat[app.human.locX][app.human.locY].bottle, 
                app.human, app.robot)
    elif event.key in CANVAS.DIR["robot"].keys() :
        dir = CANVAS.DIR["robot"][event.key]
        if chamberQuery(app, app.maze, app.robot, dir) :
            app.robot.moveDir(app.maze, dir)
            BottlePicker.run(app.maze.mat[app.robot.locX][app.robot.locY].bottle, 
                app.robot, app.human)
    
    resp, msg = GameOver.check(app.maze, app.human, app.robot) 
    if resp :
        print ("game over")
        app.gameover = True
        app.msg = msg
    


# TODO: fix this
def displayMsg(app, canvas) :
    canvas.create_oval(650, 80, 674, 104, fill=CANVAS.human_color, outline=CANVAS.human_color)
    canvas.create_text(680, 100, text = "memory: " + str(app.human.memory), 
        anchor = "sw", font="Times 20")
    canvas.create_text(680, 120, text = "vision: " + str(app.human.vision), 
        anchor = "sw", font="Times 20")
    canvas.create_text(680, 140, text = "speed: " + str(app.human.speed), 
        anchor = "sw", font="Times 20")
    canvas.create_oval(650, 180, 674, 204, fill=CANVAS.robot_color,outline=CANVAS.robot_color)
    canvas.create_text(680, 200, text = "memory: " + str(app.robot.memory), 
        anchor = "sw", font="Times 20")
    canvas.create_text(680, 220, text = "vision: " + str(app.robot.vision), 
        anchor = "sw", font="Times 20")
    canvas.create_text(680, 240, text = "speed: " + str(app.robot.speed), 
        anchor = "sw", font="Times 20")
    if app.winner != None :
        if app.winner == 'human' :
            canvas.create_oval(675, 350, 725, 400, fill=CANVAS.human_color, outline=CANVAS.human_color)
        else :
            canvas.create_oval(675, 350, 725, 400, fill=CANVAS.robot_color, outline=CANVAS.robot_color)
        canvas.create_text(700, 420, text = app.msg,
            font="Times 25 bold")

def drawMsgBox(app, canvas):
    pass
    
    
def redrawAll(app, canvas):
    drawMaze(app, canvas)
    displayMsg(app, canvas)


def run():
    runApp(width=CANVAS.width, height=CANVAS.height)