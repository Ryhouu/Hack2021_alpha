from Frame import Player, Bottle, Maze
from _config import CANVAS

def isChamber(maze, x, y) :
    return maze.isValidEntry(x, y) and maze.mat[x][y].isChamber()

def isBomb(maze, x, y) :
    return maze.mat[x][y].bottle is not None and maze.mat[x][y].bottle.isBomb()

def getLoc(maze : Maze, player : Player, dir : str) :
    delta = CANVAS.DIR["delta"]
    dx, dy = delta[dir][0], delta[dir][1]
    px, py = player.locX, player.locY
    return px + dx, py + dy

def run(maze : Maze, player : Player, dir : str) :
    pass