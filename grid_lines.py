"""
Module to manage grid lines drawing on a separate surface.
"""

import pygame

from color_set import Colors


class GridLines:
    """Class responsible for managing grid lines as a static component."""

    GRID_LINE_COLOR = Colors.DARK35.value

    def __init__(self, width, height, cell_size):
        self.rows = height // cell_size
        self.columns = width // cell_size

        self.cell_size = cell_size
        self.grid_surface = pygame.Surface((width, height))
        self.visible = True

        # Draw the grid lines initially
        self._draw_grid_lines()

    def _draw_grid_lines(self):
        """Draw grid lines on the static grid surface."""
        self.grid_surface.fill(Colors.BLACK.value)
        for row in range(self.rows):
            for column in range(self.columns):
                rect = pygame.Rect(
                    column * self.cell_size,
                    row * self.cell_size,
                    self.cell_size,
                    self.cell_size,
                )
                pygame.draw.rect(self.grid_surface, GridLines.GRID_LINE_COLOR, rect, 1)

    def toggle_visibility(self):
        """Toggle the visibility of the grid lines."""
        self.visible = not self.visible

    def get_surface(self):
        """Get the grid lines surface to be blitted, if visible."""
        return self.grid_surface if self.visible else None
