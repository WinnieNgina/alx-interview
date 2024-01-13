#!/usr/bin/python3
"""Using backtracking to solve the nqueens problem"""
import sys


def is_safe(board, row, col, N):
    """Check if there is a queen in the same column or diagonals"""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """ finds all possible solutions to the
    N-Queens problem for a given board size N."""
    solutions = []

    def backtrack(row, board):
        """If all queens are placed successfully,
        add the solution to the list"""
        if row == N:
            solution_coordinates = []
            for i in range(N):
                solution_coordinates.append([i, board[i]])
            solutions.append(solution_coordinates)
            return

        # Try placing a queen in each column of the current row
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                # Recursively move on to the next row
                backtrack(row + 1, board)

    # Initialize the board with all queens initially placed outside the board
    board = [-1] * N
    backtrack(0, board)
    return solutions


if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check if N is greater than or equal to 4
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve and print the N-Queens solutions
    solutions = solve_nqueens(N)

    for solution in solutions:
        print(solution)
