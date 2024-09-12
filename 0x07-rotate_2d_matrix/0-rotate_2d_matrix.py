#!/usr/bin/python3

"""
2D Matrix Rotation Module

This module contains a function `rotate_2d_matrix` which rotates a given
n x n 2D matrix 90 degrees clockwise in place.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in place.

    This function first transposes the matrix (swapping rows and columns),
    and then reverses each row to achieve the 90-degree clockwise rotation.

    Args:
        matrix (list of list of int): A 2D matrix represented as
        a list of lists.

    Returns:
        None: The rotation is done in place, so the input matrix is
        modified directly.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i] = matrix[i][::-1]
