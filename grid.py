"""
Creating the grid and fill it with 1s and 0s.
"""

import random

import pygame

from color_set import Colors


class Grid:
    """ "Grid Class with Sapres Representation"""

    LIVE_CELL_COLOR = Colors.LIGHT181.value
    DEAD_CELL_COLOR = Colors.DARK20.value
    GRID_LINE_COLOR = Colors.LIGHT181.value

    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size  # no. of rows: 1500 // 25 = 60
        self.columns = width // cell_size  # no. of columns: 1500 // 25 = 60
        self.cell_size = cell_size
        # self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]
        self.cells = {}  # Dictionary to store only live cells
        self.draw_grid_lines = True  # Default gird lines is False

    def draw(self, window):
        """To draw grid using spares representation"""

        # Check all cells, if cell is a live, color it green, else dark gray.
        for row, column in self.cells:
            color = Grid.LIVE_CELL_COLOR
            pygame.draw.rect(
                window,
                color,
                (
                    column * self.cell_size,  # x position
                    row * self.cell_size,  # y position
                    self.cell_size - 0.5,  # width. -1 makes cell width smaller
                    self.cell_size - 0.5,  # height. -1 makes cell height smaller
                ),
            )

        # Draw grid lines
        if self.draw_grid_lines:
            for row in range(self.rows):
                for column in range(self.columns):
                    rect = pygame.Rect(
                        column * self.cell_size,
                        row * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    )
                    pygame.draw.rect(window, Grid.GRID_LINE_COLOR, rect, 1)

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

    def toggle_grid_lines(self):
        """Toggle the drawing of grid lines"""
        self.draw_grid_lines = not self.draw_grid_lines
