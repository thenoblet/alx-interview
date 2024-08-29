# N-Queens Solver

## Overview

The N-Queens Solver is a Python script designed to solve the classic N-Queens problem. The objective of this problem is to place `N` queens on an `N x N` chessboard such that no two queens threaten each other. The solution uses a backtracking algorithm to explore all possible configurations and find all valid arrangements of queens on the board.

## Features

- **Backtracking Algorithm**: Utilizes a recursive backtracking approach to find all possible solutions to the N-Queens problem.
- **Command-Line Interface**: Accepts an integer `N` as a command-line argument and outputs all solutions in a specified format.
- **Input Validation**: Ensures that the input is a valid integer greater than or equal to 4.


## Usage
1. **Run the Script**

   ```sh
   ./nqueens.py N
   ```

   Replace `N` with the size of the chessboard and the number of queens. For example, to solve the 8-Queens problem:

   ```sh
   ./nqueens.py 8
   ```

## Examples

### Valid Input

**Command:**

```sh
./nqueens.py 4
```

**Output:**

```plaintext
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
```

Each line represents one solution, with the format `[[column, row], ...]`, where each pair denotes the position of a queen on the board.

### Invalid Input

1. **Wrong Number of Arguments**

   **Command:**

   ```sh
   ./nqueens.py
   ```

   **Output:**

   ```plaintext
   Usage: nqueens N
   ```

2. **Non-integer Input**

   **Command:**

   ```sh
   ./nqueens.py abc
   ```

   **Output:**

   ```plaintext
   N must be a number
   ```

3. **Integer Less Than 4**

   **Command:**

   ```sh
   ./nqueens.py 3
   ```

   **Output:**

   ```plaintext
   N must be at least 4
   ```

## Code Explanation

- **`is_safe(board, row, col, n)`**: Checks if it's safe to place a queen at the specified position by ensuring no two queens threaten each other.
- **`solve_nqueens(n)`**: Main function to solve the N-Queens problem using backtracking. It generates all valid configurations for placing queens on the board.
- **`print_solutions(solutions)`**: Formats and prints all found solutions.
- **`main()`**: Handles command-line arguments, performs input validation, and orchestrates the solving and printing of solutions.