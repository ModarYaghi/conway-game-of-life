"""
Creating the grid and fill it with 1s and 0s.
"""

import random

import pygame


class Grid:
    """ "Grid Class"""
    LIVE_CELL_COLOR = (0, 255, 0)
    DEAD_CELL_COLOR = (20, 20, 20)
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
                color = Grid.LIVE_CELL_COLOR if self.cells[row][column] else Grid.DEAD_CELL_COLOR

                # Check all cells, if cell is a live, color it green, else dark gray.
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

    def fill_random(self):
        """Filling the grid with random 1s and 0s"""

        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = random.choice(
                    [1, 0, 0, 0]
                )  # 25% of the cells will be filled with 1

    def clear(self):
        """Clear the grid"""
        for row in range(self.rows):
            for column in range(self.columns):
                self.cells[row][column] = 0
    
    def toggle_cell(self, row, column):
        """Toggle which cell is a live"""
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.cells[row][column] = not self.cells[row][column]