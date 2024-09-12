# 2D Matrix Rotation - Python

This repository contains a Python module that performs an in-place rotation of a 2D matrix (n x n) by 90 degrees clockwise. The code is written in Python and operates directly on the input matrix without requiring any additional space.


## Overview

The **2D Matrix Rotation** module provides a function `rotate_2d_matrix(matrix)` that modifies the input matrix directly to rotate it by 90 degrees clockwise. 

### Input Matrix Example:

```
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### Rotated Matrix:

```
[
    [7, 4, 1],
    [8, 5, 2],
    [9, 6, 3]
]
```

## Usage

The main function provided in this repository is `rotate_2d_matrix(matrix)`, which rotates the matrix in place.

```python
from matrix_rotation import rotate_2d_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)
print(matrix)
# Output:
# [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]
```

### Function Signature:
```python
def rotate_2d_matrix(matrix):
    """
    Rotates a given n x n 2D matrix 90 degrees clockwise in place.

    Args:
        matrix (list of list of int): A 2D matrix represented as a list of lists.

    Returns:
        None: The rotation is done in place, so the input matrix is modified directly.
    """
```

## Example

1. Create a 2D matrix:
    ```python
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ```

2. Call the function:
    ```python
    rotate_2d_matrix(matrix)
    ```

3. After rotation, the matrix will be:
    ```python
    [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    ```

## How It Works

The function works in two steps:

1. **Transpose the Matrix**: 
    - This step swaps rows with columns. For example, element `matrix[i][j]` is swapped with `matrix[j][i]` for all `i` and `j`. After transposing the matrix, the rows become columns.

2. **Reverse Each Row**:
    - After transposing, each row is reversed to achieve the 90-degree clockwise rotation.

### Example Walkthrough:

Given the matrix:
```python
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

- **Transpose**: 
  ```python
  [
      [1, 4, 7],
      [2, 5, 8],
      [3, 6, 9]
  ]
  ```

- **Reverse Each Row**:
  ```python
  [
      [7, 4, 1],
      [8, 5, 2],
      [9, 6, 3]
  ]
  ```
