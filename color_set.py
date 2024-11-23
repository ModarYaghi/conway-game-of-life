"""Just a including a color set for cleaner code"""

from enum import Enum


class Colors(Enum):
    """Core class"""

    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    DARK20 = (20, 20, 20)
    DARK35 = (35, 35, 35)
    LIGHT181 = (181, 181, 181)
