from Frame import Player, Bottle, Maze

def get_player_position (player: Player):
    # get the player's position in the matrix
    x = player.locX
    y = player.locY
    return (x,y)

def left_chamber (maze: Maze, player: Player):
    x = get_player_position(player)[0]
    y = get_player_position(player)[1]
    return maze.mat[x-1][y].isChamber()
    
def right_chamber (maze: Maze, player: Player):
    x = get_player_position(player)[0]
    y = get_player_position(player)[1]
    return maze.mat[x+1][y].isChamber()

def up_chamber (maze: Maze, player: Player):
    x = get_player_position(player)[0]
    y = get_player_position(player)[1]
    return maze.mat[x][y+1].isChamber()

def down_chamber (maze: Maze, player: Player):
    x = get_player_position(player)[0]
    y = get_player_position(player)[1]
    return maze.mat[x][y-1].isChamber()