#!/usr/bin/python3

"""
N-Queens Solver

This script solves the N-Queens problem using a backtracking algorithm.
It finds all possible solutions to place N queens on an NxN chessboard
such that no two queens threaten each other.

The script accepts an integer N as a command-line argument and prints
all solutions where each solution is a list of positions of queens on
the board.

Usage:
    ./nqueens N

Where N is the size of the chessboard and the number of queens.
N must be at least 4 to have a valid solution.

"""

import sys


def is_safe(board, row, col, n):
    """
    Checks if placing a queen at (row, col) is safe.

    Args:
        board (list): A list representing the board where board[i] = row
                      indicates the row position of the queen in column i.
        row (int): The row to check for safety.
        col (int): The column to place the queen.
        n (int): The size of the board.

    Returns:
        bool: True if it's safe to place the queen at (row, col),
        False otherwise.
    """
    # Check this row on left side
    for i in range(col):
        if board[i] == row:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(col-1, -1, -1), range(row-1, -1, -1)):
        if board[i] == j:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(col-1, -1, -1), range(row+1, n)):
        if board[i] == j:
            return False

    return True


def solve_nqueens(n):
    """
    Solves the N-Queens problem and finds all possible solutions.

    Args:
        n (int): The size of the board and the number of queens.

    Returns:
        list: A list of solutions where each solution is a list of
        [column, row] positions.
    """
    board = [-1] * n
    solutions = []

    def solve(col):
        """
        Recursive helper function to solve the N-Queens problem using
        backtracking.

        Args:
            col (int): The current column to place the queen.
        """
        if col == n:
            solution = [[i, board[i]] for i in range(n)]
            solutions.append(solution)
            return

        for row in range(n):
            if is_safe(board, row, col, n):
                board[col] = row
                solve(col + 1)
                board[col] = -1

    solve(0)
    return solutions


def print_solutions(solutions):
    """
    Prints the solutions in a readable format.

    Args:
        solutions (list): A list of solutions where each solution is a list of
        [column, row] positions.
    """
    for solution in solutions:
        print(solution)


def main():
    """
    Main function to handle command-line arguments and print solutions.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(n)
    print_solutions(solutions)


if __name__ == "__main__":
    main()
