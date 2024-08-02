# Lockboxes Unlocking Utility

## Overview

This project provides a utility function, `canUnlockAll`, which determines if all boxes in a set can be unlocked given a list of boxes where each box contains a list of keys to other boxes. This function is useful in scenarios where you need to ensure that every item (or box) can be accessed starting from an initial state.

## Problem Statement

You have `n` locked boxes, numbered from `0` to `n-1`. Each box may contain keys to other boxes. The goal is to determine if all boxes can be unlocked, starting from the first box (`boxes[0]`), which is unlocked initially.

### Function Prototype

```python
def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked starting from the first box.

    Parameters:
    boxes (List[List[int]]): A list of lists where each inner list
    contains integers representing keys to other boxes.

    Returns:
    bool: True if all boxes can be unlocked, False otherwise.
    """
```

## Description

### Input

- **`boxes`**: A list of lists, where each inner list contains keys (represented as integers) that open other boxes.

### Output

- **Returns**: `True` if all boxes can be unlocked; otherwise, `False`.

### How It Works

1. **Initialisation**:
   - Start with the first box (`box 0`), which is initially unlocked.
   - Create a list called `unlocked` to keep track of which boxes have been unlocked.
   - Use a `stack` to manage the boxes that need to be explored.

2. **DFS Traversal**:
   - The process is similar to Depth-First Search (DFS):
     - Pop a box from the stack.
     - For each key in the box, check if it opens a new box.
     - If a key opens a new box, mark it as unlocked and push it onto the stack for further exploration.

3. **Completion Check**:
   - After processing all reachable boxes, check if all boxes have been unlocked. If all entries in the `unlocked` list are `True`, return `True`; otherwise, return `False`.

### Example

Given the following list of boxes:

```python
boxes = [[1], [2], [3], [4], []]
```

1. **Initialization**:
   - `unlocked = [True, False, False, False, False]`
   - `stack = [0]` (Start with box 0)

2. **Processing Box 0**:
   - Keys in box 0: `[1]`
   - Mark box 1 as unlocked: `unlocked = [True, True, False, False, False]`
   - Add box 1 to the stack: `stack = [1]`

3. **Processing Box 1**:
   - Keys in box 1: `[2]`
   - Mark box 2 as unlocked: `unlocked = [True, True, True, False, False]`
   - Add box 2 to the stack: `stack = [2]`

4. **Processing Box 2**:
   - Keys in box 2: `[3]`
   - Mark box 3 as unlocked: `unlocked = [True, True, True, True, False]`
   - Add box 3 to the stack: `stack = [3]`

5. **Processing Box 3**:
   - Keys in box 3: `[4]`
   - Mark box 4 as unlocked: `unlocked = [True, True, True, True, True]`
   - Add box 4 to the stack: `stack = [4]`

6. **Processing Box 4**:
   - Keys in box 4: `[]` (No keys)
   - All boxes are now unlocked.

7. **Completion**:
   - All boxes have been visited: `unlocked = [True, True, True, True, True]`
   - Function returns `True`.

## Usage

### Example Code

```python
from lockboxes import canUnlockAll

# Test cases
boxes1 = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes1))  # Output: True

boxes2 = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes2))  # Output: True

boxes3 = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes3))  # Output: False
```


