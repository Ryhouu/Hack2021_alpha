from Session.cmu_112_graphics import *
from _config import MAZE

rawMat = MAZE.default_mat

def appStarted(app):
    app.human = Player (1, 1)
    app.x1 = 30
    app.x2 = 540
    app.y1 = 30
    app.y2 = 540


def drawMaze(app, canvas):
    
    color = ['black', 'white']
    for i in range(MAZE.width):
        for j in range(MAZE.height):
            canvas.create_rectangle(i*30, j*30, i*30+30, j*30+30, fill = app.maze.mat[i][j].color)
    canvas.create_oval(app.x1+3, app.y1+3, app.x1+27, app.y1+27, fill = 'blue')
    canvas.create_oval(app.x2+3, app.y2+3, app.x2+27, app.y2+27, fill = 'red')


def keyPressed(app, event):
    if event.key =='d':
        app.x1 += 30
        if rawMat[app.x1//30][app.y1//30] == 0 :
            app.x1 -= 30
    elif event.key =='a':
        app.x1 -= 30
        if rawMat[app.x1//30][app.y1//30] == 0 :
            app.x1 += 30
    elif event.key =='s':
        app.y1 += 30
        if rawMat[app.x1//30][app.y1//30] == 0 :
            app.y1 -= 30
    elif event.key =="w":
        app.y1 -= 30
        if rawMat[app.x1//30][app.y1//30] == 0 :
            app.y1 += 30
    
    if event.key =='Right':
        app.x2 += 30
        if rawMat[app.x2//30][app.y2//30] == 0 :
            app.x2 -= 30
    elif event.key =='Left':
        app.x2 -= 30
        if rawMat[app.x2//30][app.y2//30] == 0 :
            app.x2 += 30
    elif event.key =='Down':
        app.y2 += 30
        if rawMat[app.x2//30][app.y2//30] == 0 :
            app.y2 -= 30
    elif event.key =="Up":
        app.y2 -= 30
        if rawMat[app.x2//30][app.y2//30] == 0 :
            app.y2 += 30
    
def redrawAll(app, canvas):
    drawMaze(app, canvas)

def run():
    runApp(width=600, height=600)