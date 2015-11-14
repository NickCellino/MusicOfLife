import pygame, sys
from pygame.locals import *
from GameOfLife import GameOfLife
from SquareGridUI import SquareGridUI
from colors import *

resolution = (800, 800)

# Global initialization
pygame.init()
pygame.display.set_caption("Game of Life")
DISPLAYSURF = pygame.display.set_mode(resolution, RESIZABLE)

the_grid = SquareGridUI(DISPLAYSURF, 15, resolution[0])
the_game = GameOfLife(15, 15)
the_game.random_grid_init()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(BLACK)
    the_grid.draw_grid((0,0), the_game.grid)
    pygame.time.wait(200)
    the_game.time_step()
    pygame.display.update()
