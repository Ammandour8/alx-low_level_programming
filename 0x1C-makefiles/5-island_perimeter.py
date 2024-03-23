#!/usr/bin/python3
<<<<<<< HEAD
"""
Grid perimeter calculator module
"""


def island_perimeter(grid) -> int:
    """"Culculate the perimter of a grid
    Args:
        grid (list): A list of lists
=======
"""Defines an island perimeter measuring function."""


def island_perimeter(grid):
    """Return the perimiter of an island.

    The grid represents water by 0 and land by 1.

    Args:
        grid (list): A list of list of integers representing an island.
    Returns:
        The perimeter of the island defined in grid.
>>>>>>> 50dbb2b1d625d6106cf023b66f4fa876fadf6b6d
    """
    width = len(grid[0])
    height = len(grid)
    edges = 0
    size = 0

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                size += 1
                if (j > 0 and grid[i][j - 1] == 1):
                    edges += 1
                if (i > 0 and grid[i - 1][j] == 1):
                    edges += 1
<<<<<<< HEAD
    return (size * 4 - edges * 2)
=======
    return size * 4 - edges * 2
>>>>>>> 50dbb2b1d625d6106cf023b66f4fa876fadf6b6d
