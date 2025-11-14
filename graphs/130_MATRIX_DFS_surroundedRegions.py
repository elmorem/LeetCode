'''
You are given an `m x n` matrix `board` containing **letters** `'X'` and `'O'`, **capture regions** that are **surrounded**:

- **Connect**: A cell is connected to adjacent cells horizontally or vertically.
- **Region**: To form a region **connect every** `'O'` cell.
- **Surround**: The region is surrounded with `'X'` cells if you can **connect the region** with `'X'` cells and none of the region cells are on the edge of the `board`.

To capture a **surrounded region**, replace all `'O'`s with `'X'`s **in-place** within the original board. You do not need to return anything.

**Example 1:**

**Input:** board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

**Output:** [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

**Explanation:**

![](https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg)

In the above diagram, the bottom region
'''
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n = len(board)
        m = len(board[0])

        # If board have less than 3 size in any direction: nothing to do, because all cells located on borders
        if n < 3 or m < 3:            
            return

        # DFS to look for the next 'O' cell upper, lower, to the right and to the left of current coordinates
        # If 'O' cell is found, recursevly mark this cell as 'R' which is mean REACHED
        def dfs(row: int, col: int) -> None:
            board[row][col] = 'R'
            if row > 0 and board[row - 1][col] == 'O':
                dfs(row - 1, col)
            if row < n - 1 and board[row + 1][col] == 'O':
                dfs(row + 1, col)
            if col > 0 and board[row][col - 1] == 'O':
                dfs(row, col - 1)
            if col < m - 1 and board[row][col + 1] == 'O':
                dfs(row, col + 1)

        # Go and check left and right borders of the board
        for row in range(n):
            if board[row][0] == 'O':
                dfs(row, 0)
            if board[row][m - 1] == 'O':
                dfs(row, m - 1)

        # Same for check up and down borders of the board
        # Since corners (0,0) and (n - 1, m - 1) where checked in previous cycle, skip them in this one
        for col in range(1, m - 1):
            if board[0][col] == 'O':
                dfs(0, col)
            if board[n - 1][col] == 'O':
                dfs(n - 1, col)

        # Follow through the whole board and flip all 'R' cells back into 'O' and all 'O' cell to 'X'
        # since they're unreacheable from the board located 'O' cell if any
        for row in range(n):
            for col in range(m):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == 'R':
                    board[row][col] = 'O'

# Test cases
if __name__ == "__main__":
    solution = Solution()

    board1 = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    solution.solve(board1)
    print(board1)  # Expected output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

    board2 = [["X"]]
    solution.solve(board2)
    print(board2)  # Expected output: [["X"]]

    board3 = [["O"]]
    solution.solve(board3)
    print(board3)  # Expected output: [["O"]]

    board4 = [["X","O","X"],["O","X","O"],["X","O","X"]]
    solution.solve(board4)
    print(board4)  # Expected output: [["X","O","X"],["O","X","O"],["X","O","X"]]

    board5 = [["O","O","O"],["O","O","O"],["O","O","O"]]
    solution.solve(board5)
    print(board5)  # Expected output: [["O","O","O"],["O","O","O"],["O","O","O"]]