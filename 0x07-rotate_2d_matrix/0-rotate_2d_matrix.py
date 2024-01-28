#!/usr/bin/python3
"""Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """Given an n x n 2D matrix, rotate it 90 degrees clockwise."""
    n = len(matrix)

    # Initialize rmatrix as an empty matrix with the same dimensions
    rmatrix = [[0] * n for _ in range(n)]

    for i in range(n):
        j = n - 1
        mylist = []
        while (j >= 0):
            a = matrix[j][i]
            mylist.append(a)
            j -= 1
        rmatrix[i] = mylist

    # Copy the rotated matrix back to the original matrix
    for i in range(n):
        for j in range(n):
            matrix[i][j] = rmatrix[i][j]
