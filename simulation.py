"""Grid Simulation"""

from grid import Grid


class Simulation:
    """Simulation class"""

    def __init__(self, width, height, cell_size) -> None:
        self.grid = Grid(width, height, cell_size)
        self.temp_grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.grid.fill_random()

    def draw(self, window):
        """Draw method"""
        self.grid.draw(window)

    def count_live_neighbors(self, grid, row, column):
        """Count live neighbor"""

        live_neighbors = 0

        neighbor_offsets = [
            (-1, -1),  # dig top left
            (-1, 0),  # above
            (-1, 1),  # dig top right
            (0, -1),  # left
            (0, 1),  # right
            (1, -1),  # dig down left
            (1, 0),  # underneath
            (1, 1),  # dig down right
        ]

        for offset in neighbor_offsets:
            new_row = (row + offset[0]) % self.rows
            new_column = (column + offset[1]) % self.columns
            if self.grid.cells[new_row][new_column] == 1:  # then this neighbor is live
                live_neighbors += 1  # increasing the number of live neighbors by 1

        return live_neighbors

    def update(self):
        """Updating the simulation state according to the rules"""

        for row in range(self.rows):
            for column in range(self.columns):
                live_neighbors = self.count_live_neighbors(self.grid, row, column)
                cell_value = self.grid.cells[row][column]

                if cell_value == 1:
                    if live_neighbors > 3 or live_neighbors < 2:
                        self.temp_grid.cells[row][column] = 0
                    else:
                        self.temp_grid.cells[row][column] = 1
                else:
                    if live_neighbors == 3:
                        self.temp_grid.cells[row][column] = 1
                    else:
                        self.temp_grid.cells[row][column] = 0
        for row in range(self.rows):
            for column in range(self.columns):
                self.grid.cells[row][column] = self.temp_grid.cells[row][column]
