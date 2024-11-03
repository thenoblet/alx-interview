# Prime Game Module

This module implements a two-player mathematical game involving prime numbers.
The game is played between Maria and Ben, where they take turns choosing prime 
numbers and removing their multiples from a set of consecutive integers.

Game Rules:
1. Given a set of consecutive integers from 1 to n inclusive
2. Each player takes turns choosing a prime number from the set
3. The chosen prime number and all its multiples are removed from the set
4. The player that cannot make a move loses the game
5. Maria always goes first
6. Both players play optimally

The module provides functionality to:
- Determine if a number is prime
- Calculate valid moves for each game state
- Simulate optimal gameplay for a single round
- Determine the winner across multiple rounds

Functions:
    isPrime(num): Check if a number is prime
    get_primes_and_multiples(n): Get sets of numbers removed for each prime choice
    play_game(n): Simulate a single game with optimal play
    isWinner(x, nums): Determine winner of multiple rounds

Example:
    >>> isWinner(3, [4, 5, 1])
    'Ben'
    
    This plays 3 rounds with n values of 4, 5, and 1:
    - Round 1 (n=4): Ben wins
    - Round 2 (n=5): Maria wins
    - Round 3 (n=1): Ben wins
    Ben wins 2 rounds, so he's the overall winner