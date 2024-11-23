"""
Creating the grid and filling it with live (1) and dead (0).
"""

import random

import pygame

from color_set import Colors


class Grid:
    """ "Grid Class with Spares Representation"""

    LIVE_CELL_COLOR = Colors.LIGHT181.value
    DEAD_CELL_COLOR = Colors.DARK20.value
    GRID_LINE_COLOR = Colors.DARK35.value

    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size  # no. of rows: 1500 // 25 = 60
        self.columns = width // cell_size  # no. of columns: 1500 // 25 = 60
        self.cell_size = cell_size
        self.cells = {}  # Dictionary to store only live cells

    def draw(self, window):
        """Draw all live cells on the given window, including static grid lines if enabled."""

        # Draw all live cells
        for row, column in self.cells:
            pygame.draw.rect(
                window,
                Grid.LIVE_CELL_COLOR,
                (
                    column * self.cell_size + 1,  # x position offset to show grid lines
                    row * self.cell_size + 1,  # y position offset to show grid lines
                    self.cell_size
                    - 2,  # width. Slight adjustment to leave room for gird lines
                    self.cell_size
                    - 2,  # height. Slight adjustment to leave room for grid lines
                ),
            )

    def fill_random(self):
        """Filling the grid with random 1s and 0s"""

        self.cells.clear()

        for row in range(self.rows):
            for column in range(self.columns):
                if random.choice([True, False, False, False]):
                    self.cells[(row, column)] = 1

    def clear(self):
        """Clear the grid"""
        self.cells.clear()

    def toggle_cell(self, row, column):
        """Toggle the state of a cell"""
        if (row, column) in self.cells:
            del self.cells[(row, column)]
        else:
            self.cells[(row, column)] = 1
