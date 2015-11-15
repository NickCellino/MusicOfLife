import pygame, sys
from pygame.locals import *
from GameOfLife import GameOfLife
from SquareGridUI import SquareGridUI
from colors import *
from music import LifeAudio

resolution = (800, 800)
board_size = 35
gaps = 1
time_per_col = .15

# Global initialization
pygame.init()
pygame.display.set_caption("Game of Life")
DISPLAYSURF = pygame.display.set_mode(resolution, RESIZABLE)

the_grid = SquareGridUI(DISPLAYSURF, board_size, resolution[0], gaps)
the_game = GameOfLife(board_size, board_size)
the_game.random_grid_init()
# the_game.insert_pulsar((1, 1))
# the_game.insert_pulsar((17, 17))

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
            the_grid.color_square(current_column, row, MAT_AMBER)
        else:
            the_grid.color_square(current_column, row, BLUE_GREY_HIGH)
    current_column = (current_column + 1) % the_game.grid.getWidth()

    pygame.display.update()
    if len(alive_rows) != 0:
        audio.play_notes(alive_rows, time_per_col)
    else:
        pygame.time.wait(int(time_per_col*1000))

    the_game.time_step()
