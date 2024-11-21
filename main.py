"""
Game of Life Rules

The game has four Rules

    1. Underoppulation: A live cell with fewer than two live neighbors dies.
    2. Stasis: A live cell with two or three live neighbors lives on to the next generation.
    3. Overpopulation: A live cell with more than three live neighbors dies.
    4. Reproduction: A dead cell with exactly three live neighbors becomes a live cell.
"""

import sys

import pygame

from color_set import Colors
from simulation import Simulation

pygame.init()

BACKGROUND_COLOR = Colors.BLACK.value
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 1500
CELL_SIZE = 15
FPS = 12

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()

# Create Grid object
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)

# Simulation Loop
while True:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            row = pos[1] // CELL_SIZE
            column = pos[0] // CELL_SIZE
            simulation.toggle_cell(row, column)

        # if a key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

            elif event.key == pygame.K_SPACE:
                if simulation.is_running():
                    simulation.stop()
                    pygame.display.set_caption("Game of Life has stopped")
                else:
                    simulation.start()
                    pygame.display.set_caption(f"Game of Life is running on FPS {FPS}")

            elif event.key == pygame.K_f:
                FPS += 2
                pygame.display.set_caption(f"Game of Life is running on FPS {FPS}")

            elif event.key == pygame.K_s:
                if FPS > 5:
                    FPS -= 2
                pygame.display.set_caption(f"Game of Life is running on FPS {FPS}")

            elif event.key == pygame.K_r:
                simulation.create_random_state()

            elif event.key == pygame.K_c:
                simulation.clear()

            elif event.key == pygame.K_g:
                simulation.grid.toggle_grid_lines()

    # 2. Updating State
    simulation.update()

    # 3. Drawing
    window.fill(BACKGROUND_COLOR)
    simulation.draw(window)  # calling drow method from Grid

    pygame.display.update()
    clock.tick(FPS)
