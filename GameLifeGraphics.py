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
# the_game.random_grid_init()
the_game.insert_pulsar((2, 2))

audio = LifeAudio()
current_column = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(BLUE_GREY)
    the_grid.draw_grid((0,0), the_game.grid, BLUE_GREY, MAT_ORANGE)

    alive_rows = []
    for row in range(the_game.grid.getHeight()):
        if the_game.grid[current_column][row] == GameOfLife.ALIVE:
            alive_rows.append(row)
            the_grid.color_square(current_column, row, MAT_GREY)
    current_column = (current_column + 1) % the_game.grid.getWidth()

    pygame.display.update()
    if len(alive_rows) != 0:
        audio.play_notes(alive_rows, 0.25)
    else:
        pygame.time.wait(250)

    the_game.time_step()
