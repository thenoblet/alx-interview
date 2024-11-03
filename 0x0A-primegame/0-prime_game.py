#!/usr/bin/env python3

""" Prime number game """


def isPrime(num):
    """
    Check if a number is prime.
    Args:
        num: number to check
    Returns:
        bool: True if prime, False otherwise
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes_and_multiples(n):
    """
    Get set of numbers that will be removed when choosing each prime up to n.
    Args:
        n: upper limit
    Returns:
        dict: prime number -> set of numbers that would be removed
    """
    moves = {}
    for i in range(2, n + 1):
        if isPrime(i):
            removed = set()
            for j in range(i, n + 1, i):
                removed.add(j)
            moves[i] = removed
    return moves


def play_game(n):
    """
    Simulate a single game with optimal play.
    Args:
        n: upper limit of number set
    Returns:
        bool: True if Maria wins, False if Ben wins
    """
    if n < 2:  # No prime numbers available for first move
        return False

    # Get all possible moves and their impacts
    numbers = set(range(1, n + 1))
    moves = get_primes_and_multiples(n)

    def get_valid_moves():
        return [p for p in moves.keys() if p in numbers]

    # Maria's turn (True = Maria's turn, False = Ben's turn)
    turn = True

    while True:
        valid_moves = get_valid_moves()

        if not valid_moves:  # No valid moves left
            return not turn  # Return True if it's Ben's turn (Maria won)

        # Choose the move that leaves opponent with fewest options
        best_move = valid_moves[0]
        numbers.difference_update(moves[best_move])

        turn = not turn


def isWinner(x, nums):
    """
    Determine the winner of multiple rounds of the prime game.
    Args:
        x: number of rounds
        nums: array of n values for each round
    Returns:
        str: name of player with most wins, or None if tied
    """
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    for n in nums[:x]:  # Only play x rounds
        if play_game(n):
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
