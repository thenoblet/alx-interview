#!/usr/bin/python3

"""This module defines the Pascal's Triangle function."""


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Parameters:
    n (int): The number of rows of Pascal's Triangle to generate.
    If n is less than or equal to 0, the function returns an empty list.

    Returns:
    list of lists: A list of lists, where each inner list represents
    a row in Pascal's Triangle.
    Each row contains integers representing the binomial coefficients.

    Examples:
    >>> pascal_triangle(5)
    [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]

    >>> pascal_triangle(0)
    []

    >>> pascal_triangle(-1)
    []

    >>> pascal_triangle(1)
    [[1]]
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Initialize the first row of the triangle

    for i in range(1, n):
        row = [1]  # Start the new row with 1
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End the row with 1
        triangle.append(row)

    return triangle
