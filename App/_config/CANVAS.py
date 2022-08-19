width = 800
height = 600

maze_width = 600
maze_height = 600

DIR = {
    "human" : {
        "w" : "N",
        "s" : "S",
        "a" : "W", 
        "d" : "E"
    },
    "robot" : {
        "Up" : "N",
        "Down" : "S",
        "Left" : "W", 
        "Right" : "E"
    },
    "delta" : {
        "W" : (-1, 0),
        "E" : (1, 0),
        "N" : (0, -1),
        "S" : (0, 1)
    }
}

human_color = "#191970"
robot_color = "#556B2F"