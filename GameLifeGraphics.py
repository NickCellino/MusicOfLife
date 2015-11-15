import pygame, sys
from pygame.locals import *
from GameOfLife import GameOfLife
from SquareGridUI import SquareGridUI
from colors import *
from music import LifeAudio

resolution = (800, 800)
board_size = 20

# Global initialization
pygame.init()
pygame.display.set_caption("Game of Life")
DISPLAYSURF = pygame.display.set_mode(resolution, RESIZABLE)

the_grid = SquareGridUI(DISPLAYSURF, board_size, resolution[0])
the_game = GameOfLife(board_size, board_size)
the_game.random_grid_init()

audio = LifeAudio()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(RED)
    the_grid.draw_grid((0,0), the_game.grid)
    pygame.display.update()

    for column in range(the_game.grid.getWidth()):
        alive_rows = []
        for row in range(the_game.grid.getHeight()):
            if the_game.grid[column][row] == GameOfLife.ALIVE:
                alive_rows.append(row)
        audio.play_notes(alive_rows, 0.25)

    the_game.time_step()
    # pygame.time.wait(100)
