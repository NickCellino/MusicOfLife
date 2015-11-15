import pygame, sys
from pygame.locals import *
from GameOfLife import GameOfLife
from SquareGridUI import SquareGridUI
from colors import *
from music import LifeAudio

resolution = (1000, 1000)
board_size = 30
gaps = 1
time_per_col = .5

# Global initialization
pygame.init()
pygame.display.set_caption("The Music of Life")
DISPLAYSURF = pygame.display.set_mode(resolution, RESIZABLE)

the_grid = SquareGridUI(DISPLAYSURF, board_size, resolution[0], gaps)
the_game = GameOfLife(board_size, board_size)
the_game.random_grid_init()

audio = LifeAudio()
current_column = 0
column_dir = 1
current_row = 0
row_dir = 1
paused = False

def toggle_pause():
    global paused
    paused = not paused

def increase_speed():
    global time_per_col
    if time_per_col > .05:
        time_per_col -= .025

def decrease_speed():
    global time_per_col
    time_per_col += .025

def is_on_grid(position):
    if position[0] > 0 and position[0] < resolution[0]:
        if position[1] > 0 and position[1] < resolution[1]:
            return True
    return False

def highlight_current_mouse_position():
    global the_grid
    mouse_position = pygame.mouse.get_pos()
    if is_on_grid(mouse_position):
        square_location = the_grid.get_square_location(mouse_position)
        the_grid.color_square(square_location[0], square_location[1], BLUE_GREY_HIGH)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                toggle_pause()
            elif event.key == K_UP:
                increase_speed()
            elif event.key == K_DOWN:
                decrease_speed()
            elif event.key == K_r:
                the_game.reset_grid()
            elif event.key == K_RETURN:
                the_game.random_grid_init()
            elif event.key == K_g:
                mouse_position = pygame.mouse.get_pos()
                if is_on_grid(mouse_position):
                    square_location = the_grid.get_square_location(mouse_position)
                    the_game.insert_glider(square_location)
            elif event.key == K_p:
                mouse_position = pygame.mouse.get_pos()
                if is_on_grid(mouse_position):
                    square_location = the_grid.get_square_location(mouse_position)
                    loc = (square_location[0] - 7, square_location[1] - 7)
                    the_game.insert_pulsar(loc)
        if event.type == MOUSEBUTTONUP:
            if paused:
                mouse_position = pygame.mouse.get_pos()
                if is_on_grid(mouse_position):
                    square_location = the_grid.get_square_location(mouse_position)
                    if the_game.grid[square_location[0]][square_location[1]] == GameOfLife.ALIVE:
                        the_game.grid[square_location[0]][square_location[1]] = GameOfLife.DEAD
                    else:
                        the_game.grid[square_location[0]][square_location[1]] = GameOfLife.ALIVE
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
        the_grid.draw_grid((0,0), the_game.grid, BLUE_GREY, MAT_ORANGE)
        highlight_current_mouse_position()
        pygame.display.update()
