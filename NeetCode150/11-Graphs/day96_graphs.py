"""Day 96 — NeetCode 150: Graphs
Surrounded Regions (LC 130) — Medium
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Reverse border DFS/BFS:
        1. Any 'O' connected to the border cannot be surrounded.
        2. Traverse from border 'O's and mark them as non-surrounded (e.g., 'T').
        3. Capture remaining 'O's to 'X', then revert 'T's back to 'O'.
        """
        rows, cols = len(board), len(board[0])

        def dfs(r: int, c: int) -> None:
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # Step 1: Mark border-connected 'O's
        for r in range(rows):
            if board[r][0] == "O":
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                dfs(r, cols - 1)

        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)

        # Step 2: Convert surrounded 'O' -> 'X', restore 'T' -> 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"