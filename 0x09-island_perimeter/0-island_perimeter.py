#!/usr/bin/python3
"""returns the perimeter of the island described in grid"""


def island_perimeter(grid):
    """grid is a list of list of integers:
    0 represents water
    1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    """
    perimeter = 0
    index = 0
    for i in range(len(grid)):
        for j in range(len(grid[1])-1, -1, -1):
            if grid[i][j] == 1:
                index = (j + 1) * 2
        perimeter += index
        index = 0
    return perimeter
