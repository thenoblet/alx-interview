#!/usr/bin/python3

"""
Island Perimeter Module

This module contains a function `island_perimeter` which calculates the
perimeter of an island represented by a grid of 0s and 1s.

In the grid, 1s represent land and 0s represent water. The perimeter
is defined as the length of the boundary of the island.

Example:
    Given the following grid:
    [
        [0, 1, 0, 0],
        [1, 1, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]

    The perimeter of the island would be 12.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of an island in a grid.

    The perimeter is calculated based on the number of edges of land cells
    (1s) that are adjacent to water cells (0s) or the grid boundary.

    Args:
        grid (list of list of int): A 2D grid representing the island, where
                                     1 represents land and 0 represents water.

    Returns:
        int: The perimeter of the island.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Start with 4 sides for each land cell

                # Check and subtract for adjacent land cells
                if i > 0 and grid[i-1][j] == 1:
                    perimeter -= 1
                if i < rows-1 and grid[i+1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j-1] == 1:
                    perimeter -= 1
                if j < cols-1 and grid[i][j+1] == 1:
                    perimeter -= 1

    return perimeter
