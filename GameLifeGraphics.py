import pygame, sys
from pygame.locals import *
from GameOfLife import GameOfLife
from SquareGridUI import SquareGridUI
from colors import *
from music import LifeAudio

resolution = (1000, 1000)
board_size = 30
gaps = 1
time_per_col = .20

# Global initialization
pygame.init()
pygame.display.set_caption("Game of Life")
DISPLAYSURF = pygame.display.set_mode(resolution, RESIZABLE)

the_grid = SquareGridUI(DISPLAYSURF, board_size, resolution[0], gaps)
the_game = GameOfLife(board_size, board_size)
the_game.random_grid_init()
# the_game.insert_pulsar((1, 1))
# the_game.insert_pulsar((17, 17))
# the_game.insert_glider((5, 5))

audio = LifeAudio()
current_column = 0
column_dir = 1
current_row = 0
row_dir = 1
paused = False

def toggle_pause():
    global paused
    paused = not paused

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                toggle_pause()
    if not paused:
        DISPLAYSURF.fill(BLUE_GREY)
        the_grid.draw_grid((0,0), the_game.grid, BLUE_GREY, MAT_ORANGE)

        alive_rows = []
        for row in range(the_game.grid.getHeight()):
            if the_game.grid[current_column][row] == GameOfLife.ALIVE:
                alive_rows.append(row)
                the_grid.color_square(current_column, row, MAT_AMBER)
            else:
                the_grid.color_square(current_column, row, BLUE_GREY_HIGH)
        current_column += column_dir 
        if current_column < 0 or current_column == the_game.grid.getWidth():
            column_dir *= -1
            current_column += 2*column_dir

        pygame.display.update()
        if len(alive_rows) != 0:
            audio.play_notes(alive_rows, time_per_col)
        else:
            pygame.time.wait(int(time_per_col*1000))

        the_game.time_step()
    if paused:
        pass
