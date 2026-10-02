"""
Day 88 — NeetCode 150: Backtracking (Final)
Letter Combinations of a Phone Number | N-Queens
"""
from typing import List

# ============================================================
# 1. LETTER COMBINATIONS OF A PHONE NUMBER (LC 17) — Medium
# ============================================================
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        DFS through a digit-to-char hash map. 
        Time: O(4^N * N) where N is length of digits.
        """
        if not digits:
            return []
            
        digit_to_char = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []

        def dfs(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            
            for c in digit_to_char[digits[i]]:
                dfs(i + 1, curStr + c)
                
        dfs(0, "")
        return res

# ============================================================
# 2. N-QUEENS (LC 51) — Hard
# ============================================================
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Track columns, positive diagonals (r + c), and negative 
        diagonals (r - c) to place queens. Backtrack if invalid.
        """
        col = set()
        posDiag = set()  # (r + c)
        negDiag = set()  # (r - c)
        
        res = []
        board = [["."] * n for _ in range(n)]
        
        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                
                # Place Queen
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"
                
                # Move to next row
                dfs(r + 1)
                
                # Remove Queen (Backtrack)
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."
                
        dfs(0)
        return res