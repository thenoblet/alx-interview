#!/usr/bin/python3

"""
This module provides a utility function for determining if all
boxes can be unlocked.

It includes the `canUnlockAll` function, which checks whether it is
possible to unlock all boxes given a list of boxes, where each box
contains a list of keys to other boxes.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked starting from the first box.

    This function checks if it is possible to unlock all boxes given a
    list of boxes, where each box contains keys to other boxes.
    It starts with the first box (index 0) and attempts to unlock all
    other boxes using the keys found in each box.

    Parameters:
    boxes (List[List[int]]): A list of lists where each inner list
    contains integers representing keys to other boxes.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.

    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()

        # Explore all keys in the current box
        for key in boxes[current_box]:
            if key < n and not unlocked[key]:
                unlocked[key] = True
                stack.append(key)

    # Check if all boxes are unlocked
    return all(unlocked)
