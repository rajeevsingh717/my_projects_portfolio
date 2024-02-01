""" Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Notice that an 'O' should not be flipped if:
- It is on the border, or
- It is adjacent to an 'O' that should not be flipped.
The bottom 'O' is on the border, so it is not flipped.
The other three 'O' form a surrounded region, so they are flipped.
"""

class Solution:

    def solve(self, board: List[List[str]]) -> None:
        n_rows, n_cols = len(board), len(board[0])

        # all "O"s in the border are unsurrounded, we find these, then traverse adjacent "O"s
        def dfs(r, c):
            if r < 0 or r == n_rows or c < 0 or c == n_cols or board[r][c] != "O":
                return
          
            board[r][c] = "T" # these are unsurrounded
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == "O" and (r in [0, n_rows - 1] or c in [0, n_cols - 1]):
                    dfs(r, c)

        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == "O": # surrounded, since can't reach border
                    board[r][c] = "X"
        
        for r in range(n_rows):
            for c in range(n_cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
