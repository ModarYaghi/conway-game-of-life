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

    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size  # no. of rows: 1500 // 25 = 60
        self.columns = width // cell_size  # no. of columns: 1500 // 25 = 60
        self.cell_size = cell_size
        self.cells = {}  # Dictionary to store only live cells

        # Create a Surface to hold all live cells
        self.cell_surface = pygame.Surface((width, height), pygame.SRCALPHA)
        self.cell_surface.fill((0, 0, 0, 0))  # Make it transparent initially

    def draw(self):
        """Update the cell surface by drawing all live cells onto it."""

        # Clear previous cell drawing
        self.cell_surface.fill(
            (0, 0, 0, 0)
        )  # Make the entire surface transparent again.

        # Draw each live cell on the surface
        for row, column in self.cells:
            pygame.draw.rect(
                self.cell_surface,
                Grid.LIVE_CELL_COLOR,
                (
                    column * self.cell_size + 1,  # x position.
                    row * self.cell_size + 1,  # y position.
                    self.cell_size - 2,  # width.
                    self.cell_size - 2,  # height.
                ),
            )

    def get_surface(self):
        """Get the surface containing the draw cells."""
        return self.cell_surface

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
