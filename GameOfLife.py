from Grid import Grid
import random

class GameOfLife:

    DEAD = 0
    ALIVE = 1

    def __init__(self, num_columns, num_rows):
        self.grid = Grid(num_rows, num_columns, GameOfLife.DEAD)

    def get_num_live_neighbors(self, column, row):
        num_live_neighbors = 0
        test_col = column - 1
        for neighbor_location in self.get_neighbor_locations(column, row):
            try:
                if self.grid[neighbor_location[0]][neighbor_location[1]] == GameOfLife.ALIVE:
                    num_live_neighbors += 1
            except IndexError:
                pass
        return num_live_neighbors

    def get_neighbor_locations(self, column, row):
        neighbor_locations = []
        neighbor_locations.append((column - 1, row - 1))
        neighbor_locations.append((column - 1, row))
        neighbor_locations.append((column - 1, row + 1))
        neighbor_locations.append((column, row + 1))
        neighbor_locations.append((column, row - 1))
        neighbor_locations.append((column + 1, row - 1))
        neighbor_locations.append((column + 1, row))
        neighbor_locations.append((column + 1, row + 1))
        return neighbor_locations

    def time_step(self):
        new_grid = Grid(self.grid.getHeight(), self.grid.getWidth())
        for column in range(self.grid.getWidth()):
            for row in range(self.grid.getHeight()):
                is_alive = self.grid[column][row] == GameOfLife.ALIVE
                num_living_neighbors = self.get_num_live_neighbors(column, row)
                if is_alive and num_living_neighbors < 2:
                    new_grid[column][row] =  GameOfLife.DEAD
                elif is_alive and (num_living_neighbors == 2 or num_living_neighbors == 3):
                    new_grid[column][row] = GameOfLife.ALIVE
                elif is_alive and num_living_neighbors > 3:
                    new_grid[column][row] =  GameOfLife.DEAD
                elif not is_alive and num_living_neighbors == 3:
                    new_grid[column][row] =  GameOfLife.ALIVE
                else:
                    new_grid[column][row] = self.grid[column][row]
        self.grid = new_grid

    def random_grid_init(self):
        for column in range(self.grid.getWidth()):
            for row in range(self.grid.getHeight()):
                rand_state = random.choice([GameOfLife.ALIVE, GameOfLife.DEAD])
                self.grid[column][row] = rand_state

if __name__ == "__main__":
    g = GameOfLife(15, 15)
    g.grid[1][1] = GameOfLife.ALIVE
    g.grid[1][2] = GameOfLife.ALIVE
    g.grid[2][2] = GameOfLife.ALIVE
    g.grid[3][3] = GameOfLife.ALIVE
    print(g.grid)
    g.time_step()
    print(g.grid)
    g.time_step()
    print(g.grid)
    g.time_step()
    print(g.grid)
