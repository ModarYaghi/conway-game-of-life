"""Grid Simulation"""

from grid import Grid


class Simulation:
    """Simulation class with Sparse Representation"""

    def __init__(self, width, height, cell_size) -> None:
        self.grid = Grid(width, height, cell_size)
        self.temp_grid = Grid(width, height, cell_size)  # A temporary grid for updates
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.run = False

    def draw_cells(self, window):
        """Draw only the live cells on the window"""
        self.grid.draw(window)

    def count_live_neighbors(self, row, column):
        """Count the number of live neighbors for a given cell"""

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
            neighbor_row = (row + offset[0]) % self.rows
            neighbor_column = (column + offset[1]) % self.columns
            if (
                neighbor_row,
                neighbor_column,
            ) in self.grid.cells:  # then this neighbor is live
                live_neighbors += 1  # increasing the number of live neighbors by 1

        return live_neighbors

    def update(self):
        """Update the simulation state according to the rules"""
        if self.is_running():
            self.temp_grid.clear()
            # Iterate over all live cells and their neighbors
            cells_to_check = set(self.grid.cells.keys())

            for row, column in self.grid.cells.keys():
                # Add neighbors to the cells to be checked
                neighbor_offset = [
                    (-1, -1),
                    (-1, 0),
                    (-1, 1),
                    (0, -1),
                    (0, 1),
                    (1, -1),
                    (1, 0),
                    (1, 1),
                ]
                for offset in neighbor_offset:
                    neighbor_row = (row + offset[0]) % self.rows
                    neighbor_column = (column + offset[1]) % self.columns
                    cells_to_check.add((neighbor_row, neighbor_column))

            for row, column in cells_to_check:
                live_neighbors = self.count_live_neighbors(row, column)
                if (row, column) in self.grid.cells:
                    # Current cell is alive
                    if live_neighbors in (2, 3):
                        self.temp_grid.cells[(row, column)] = 1
                else:
                    # Current cell is dead
                    if live_neighbors == 3:
                        self.temp_grid.cells[(row, column)] = 1

            # Swap the grids
            self.grid, self.temp_grid = self.temp_grid, self.grid

    def is_running(self):
        """To check if the simulation is running"""
        return self.run

    def start(self):
        """ "A switch key to start simulation"""
        self.run = True

    def stop(self):
        """ "A switch key to stop simulation"""
        self.run = False

    def clear(self):
        """A switch key to clear the grid"""
        if not self.is_running():
            self.grid.clear()

    def create_random_state(self):
        """Create a random state for the grid"""
        if not self.is_running():
            self.grid.fill_random()

    def toggle_cell(self, row, column):
        """Toggle the state of a cell"""
        if not self.is_running():
            self.grid.toggle_cell(row, column)
