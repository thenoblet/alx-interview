#!/usr/bin/python3
"""
Prime Game Module

This module implements a two-player mathematical game involving prime numbers.
The game is played between Maria and Ben, where they take turns
choosing prime numbers and removing their multiples from a set of
consecutive integers.

Optimized for large inputs using the Sieve of Eratosthenes algorithm and
pre-computation of game results for faster lookup.
"""


def prime_numbers_sieve(n):
    """
    Use Sieve of Eratosthenes to generate prime numbers up to n.
    Args:
        n (int): Upper limit
    Returns:
        list: List of booleans where True indicates a prime number
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False
    return primes


def calculate_game_winners(n):
    """
    Pre-calculate winners for games up to n.
    Args:
        n (int): Maximum game size to calculate
    Returns:
        list: List where index i contains True if Maria wins game of size i
    """
    winners = [False] * (n + 1)
    primes = prime_numbers_sieve(n)

    # Handle edge cases
    if n >= 2:
        winners[2] = True  # Maria wins on n=2 by choosing 2

    # For each game size, determine winner
    for i in range(3, n + 1):
        # Count primes in range
        prime_count = sum(1 for j in range(2, i + 1) if primes[j])
        # If odd number of primes, Maria wins; if even, Ben wins
        winners[i] = prime_count % 2 == 1

    return winners


def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of the prime game.
    Args:
        x (int): number of rounds
        nums (list): array of n values for each round
    Returns:
        str: name of player with most wins ("Maria" or "Ben"), or None if tied
    """
    if not nums or x < 1 or x > 10000:
        return None

    # Find maximum n to pre-calculate winners
    max_n = max(nums)
    if max_n > 10000:
        return None

    # Pre-calculate winners for all possible game sizes
    winners = calculate_game_winners(max_n)

    # Count wins for each player
    maria_wins = sum(1 for n in nums[:x] if n > 1 and winners[n])
    ben_wins = sum(1 for n in nums[:x] if n <= 1 or not winners[n])

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
