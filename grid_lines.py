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

        # Draw horizontal lines across the entire width
        for row in range(self.rows + 1):
            y = row * self.cell_size
            pygame.draw.line(
                self.grid_surface,
                GridLines.GRID_LINE_COLOR,
                (0, y),
                (self.columns * self.cell_size, y),
                1,
            )

            # Draw vertical lines across the entire height
            for column in range(self.columns + 1):
                x = column * self.cell_size
                pygame.draw.line(
                    self.grid_surface,
                    GridLines.GRID_LINE_COLOR,
                    (x, 0),
                    (x, self.rows * self.cell_size),
                    1,
                )

    def toggle_visibility(self):
        """Toggle the visibility of the grid lines."""
        self.visible = not self.visible

    def get_surface(self):
        """Get the grid lines surface to be blitted, if visible."""
        return self.grid_surface if self.visible else None
