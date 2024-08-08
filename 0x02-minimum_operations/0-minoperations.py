#!/usr/bin/python3

"""
This module provides a function to compute the minimum number of
operations to get exactly `n` H characters on the screen using
the Copy All and Paste operations.

It includes the `minOperations` function, which calculates the minimum
number of operations required to reach `n` characters by using the
operations Copy All (which copies the current text) and Paste
(which pastes the copied text).
"""


def minOperations(n):
    """
    Compute the minimum number of operations required to get exactly
    `n` H characters on the screen.

    This function calculates the minimum number of operations needed
    to generate exactly `n` characters on the screen starting from 1
    character by repeatedly using the Copy All and Paste operations.
    It returns the sum of all divisors that are used to reach `n`.

    Parameters:
    n (int): The number of characters to generate. Must be greater than 1.

    Returns:
    int: The minimum number of operations required to get exactly `n` chars
    """

    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
