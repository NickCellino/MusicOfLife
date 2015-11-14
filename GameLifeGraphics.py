import pygame, sys
from pygame.locals import *

resolution = (800, 800)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

pygame.init()
pygame.display.set_caption("Game of Life")
DISPLAYSURF = pygame.display.set_mode(resolution, RESIZABLE)

def draw_square(surface, location, size, color):
    pygame.draw.rect(surface, color, (location[0], location[1], size, size))

def draw_square_grid(surface, num_rows_cols, location, size, color = BLACK):
    gap_size = 4
    current_location = (location[0] + gap_size, location[1] + gap_size)
    square_size = ((size - gap_size)/num_rows_cols) - gap_size
    for i in range(0, num_rows_cols):
        for j in range(0, num_rows_cols):
            draw_square(surface, current_location, square_size, color)
            current_location = (current_location[0] + square_size + gap_size, current_location[1])
        current_location = (location[0] + gap_size, current_location[1] + square_size + gap_size)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    DISPLAYSURF.fill(BLACK)
    draw_square_grid(DISPLAYSURF, 15, (0,0), 800, WHITE)
    pygame.display.update()
    pygame.time.wait(10)
