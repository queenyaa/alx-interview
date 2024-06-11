#!/usr/bin/python3
"""
Module to calculate the perimeter of an island in a grid.
The grid is represented by a 2D array of integers.
1 represents land, and 0 represents water.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of an island in a grid.

    Args:
        grid (list of list of int): 2D list representing the grid.

    Returns:
        int: The perimeter of the island.
    """
    # Get the dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    # Define the directions for the four neighbors (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Iterate over each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the current cell is land
            if grid[r][c] == 1:
                # Check each of the four neighbors
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    # If the neighbor is out of bounds or
                    # water, increment perimeter
                    if nr < 0 or nr >= rows or nc < 0 or \
                       nc >= cols or grid[nr][nc] == 0:
                        perimeter += 1

    return perimeter
