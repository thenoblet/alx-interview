#!/usr/bin/python3

"""
Coin Change Problem Solver

This module provides a solution to the coin change problem using
dynamic programming.
The problem is to find the minimum number of coins required to make
up a given total amount, given a list of coin denominations.

The main function in this module is `makeChange`, which takes a
list of coin denominations and a target total, and returns the
minimum number of coins needed to reach that total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount.

    Args:
    coins (list of int): A list of coin denominations available.
    total (int): The target amount to make change for.

    Returns:
    int: The minimum number of coins needed to make the total amount.
         Returns 0 if total is 0 or less.
         Returns -1 if the total cannot be met by any number of coins.

    Time complexity: O(total * len(coins))
    Space complexity: O(total)
    """
    if total <= 0:
        return 0

    dp = [total + 1] * (total + 1)

    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if coin <= amount:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
