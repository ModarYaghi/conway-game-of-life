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

from simulation import Simulation

pygame.init()

GREY = (29, 29, 29)
WINDOW_WIDTH = 1500
WINDOW_HEIGHT = 1500
CELL_SIZE = 25
FPS = 12

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Game of Life")

clock = pygame.time.Clock()

# Create Grid object
simulation = Simulation(WINDOW_WIDTH, WINDOW_HEIGHT, CELL_SIZE)
simulation.grid.cells[3][59] = 1

# Simulation Loop
while True:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # if a key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

    # 2. Updating State

    # 3. Drawing
    window.fill(GREY)
    simulation.draw(window)  # calling drow method from Grid

    pygame.display.update()
    clock.tick(FPS)
