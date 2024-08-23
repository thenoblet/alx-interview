#!/usr/bin/python3

"""
UTF-8 Validation Module

This module provides a function to validate whether a given list of integers
represents a valid UTF-8 encoding. UTF-8 is a variable-width character encoding
used for electronic communication. The function checks each byte to ensure it
follows the correct UTF-8 encoding rules.

Functions:
    - validUTF8(data): Validates if the input data is a valid UTF-8 encoding.
"""

from typing import List


def validUTF8(data: List[int]) -> bool:
    """
    Validates if a given list of integers represents a valid UTF-8 encoding.

    The function checks each integer in the list to determine if it conforms
    to the UTF-8 encoding rules. UTF-8 encoding uses one to four bytes for
    each character, with the first byte indicating how many bytes are used.
    Each continuation byte should start with '10' in binary.

    Args:
        data: A list of integers, where each integer represents a byte (0-255).

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    n_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for num in data:
        byte = num & 0xFF  # Ensure we are working with an 8-bit byte

        if n_bytes == 0:
            mask = mask1
            while byte & mask:
                n_bytes += 1
                mask = mask >> 1

            if n_bytes == 0:
                continue

            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    return n_bytes == 0
