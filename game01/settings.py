# This file was created by Isaiah Garcia on 10/18/23
# Contenct from Chris Bradfield; Kids can Code
# Video Link: https://youtu.be/OmlQ0XCvIn0

# game settings
WIDTH = 360
HEIGHT = 480
FPS = 30
SCORE = 0

# player settings
PLAYER_JUMP = 25
PLAYER_GRAV = 2
PLAYER_FRIC = 0.5

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40, "normal"), 
                 (WIDTH/2, HEIGHT/2 * 3 / 4, 100, 20, "moving"),
                 (125, HEIGHT - 350, 100, 20, "moving"),
                 (350, 200, 100, 20, "normal"),
                 (175, 100, 50, 20, "normal")]

