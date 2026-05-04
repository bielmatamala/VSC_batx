import pygame as PG

PG.init()

# Constants Globals de la Pantalla
SCREEN_WIDTH = PG.display.set_mode((0,0), PG.FULLSCREEN).get_width()
SCREEN_HEIGHT =  PG.display.set_mode((0,0), PG.FULLSCREEN).get_height()
SCREEN = PG.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
PG.display.set_caption("Dino_game")


game_speed = 120

# Colors
WHITE = (247, 247, 247)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)  
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (50, 50, 50)
clock = PG.time.Clock()
font = PG.font.Font("freesansbold.ttf", 36) 
