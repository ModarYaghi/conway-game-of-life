"""Grid Simulation"""

from grid import Grid


class Simulation:
    """Simulation class with Sparse Representation"""

    def __init__(self, width, height, cell_size) -> None:
        self.grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.run = False

        # New addition: Set to track live cells
        self.live_cells = set()

        self.neighbor_offsets = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]

    def draw_cells(self, window):
        """Draw only the live cells on the window"""
        self.grid.draw(window)

    def count_live_neighbors(self, row, column):
        """Count the number of live neighbors for a given cell"""

        live_neighbors = 0

        for offset in self.neighbor_offsets:
            neighbor_row = (row + offset[0]) % self.rows
            neighbor_column = (column + offset[1]) % self.columns
            if (
                neighbor_row,
                neighbor_column,
            ) in self.grid.cells:  # if this neighbor is live
                live_neighbors += 1

        return live_neighbors

    def update(self):
        """Update the simulation state according to the rules"""
        if self.is_running():
            new_live_cells = set()
            cells_to_check = set(self.live_cells)

            # Add neighbors of all live cells to cells_to_check
            for row, column in self.live_cells:
                for offset in self.neighbor_offsets:
                    neighbor_row = (row + offset[0]) % self.rows
                    neighbor_column = (column + offset[1]) % self.columns
                    cells_to_check.add((neighbor_row, neighbor_column))

            # Update the live cells set based on neighbor counts
            for row, column in cells_to_check:
                live_neighbors = self.count_live_neighbors(row, column)
                if (row, column) in self.grid.cells:
                    # Current cell is alive
                    if live_neighbors in (2, 3):
                        new_live_cells.add((row, column))
                else:
                    # Current cell is dead
                    if live_neighbors == 3:
                        new_live_cells.add((row, column))

            # Swap the grids
            self.live_cells = new_live_cells
            self.grid.cells = {cell: 1 for cell in self.live_cells}

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
            self.live_cells.clear()
            self.grid.clear()  # Delegate to Grid's clear method.

    def create_random_state(self):
        """Create a random state for the grid"""
        if not self.is_running():
            self.grid.fill_random()
            self.live_cells = set(self.grid.cells.keys())

    def toggle_cell(self, row, column):
        """Toggle the state of a cell"""
        if not self.is_running():
            if (row, column) in self.live_cells:
                self.live_cells.remove((row, column))
                del self.grid.cells[(row, column)]
            else:
                self.live_cells.add((row, column))
                self.grid.cells[(row, column)] = 1
