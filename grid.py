"""
Creating the grid and fill it with 1s and 0s.
"""

import random

import pygame


class Grid:
    """ "Grid Class"""

    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size  # no. of rows: 1500 // 25 = 60
        self.columns = width // cell_size  # no. of columns: 1500 // 25 = 60
        self.cell_size = cell_size
        self.cells = [[0 for _ in range(self.columns)] for _ in range(self.rows)]

    def draw(self, window):
        """Draw method"""

        # Check all cells, if cell is a live, color it green, else dark gray.
        for row in range(self.rows):
            for column in range(self.columns):
                color = (0, 255, 0) if self.cells[row][column] else (95, 95, 95)

                # Check all cells, if cell is a live, color it green, else dark gray.
                pygame.draw.rect(
                    window,
                    color,
                    (
                        column * self.cell_size,  # x position
                        row * self.cell_size,  # y position
                        self.cell_size - 1,  # width. -1 makes cell width smaller
                        self.cell_size - 1,  # height. -1 makes cell height smaller
                    ),
                )

    def fill_random(self):
        """Filling the grid with random 1s and 0s"""

        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = random.choice(
                    [1, 0, 0, 0]
                )  # 25% of the cells will be filled with 1
