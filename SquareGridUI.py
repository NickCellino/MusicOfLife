from GameOfLife import GameOfLife
import pygame
from pygame.locals import *
from colors import *

class SquareGridUI:

    def __init__(self, surface, num_rows_cols, size, gap_size = 5):
        self.surface = surface
        self.num_rows_cols = num_rows_cols 
        self.size = size
        self.gap_size = gap_size

    def draw_square(self, surface, location, size, color):
        pygame.draw.rect(surface, color, (location[0], location[1], size, size))

    def draw_grid(self, location, grid):
        current_location = (location[0] + self.gap_size, location[1] + self.gap_size)
        square_size = ((self.size - self.gap_size)/self.num_rows_cols) -self.gap_size 
        for i in range(0, self.num_rows_cols):
            for j in range(0, self.num_rows_cols):
                if grid[i][j] == GameOfLife.ALIVE:
                    self.draw_square(self.surface, current_location, square_size, WHITE)
                else:
                    self.draw_square(self.surface, current_location, square_size, RED)
                current_location = (current_location[0], current_location[1] + square_size + self.gap_size)
            current_location = (current_location[0] + square_size + self.gap_size, location[1] + self.gap_size)

