"""
Day 57 — NeetCode 150: Arrays & Hashing complete + Two Pointers begins
Valid Sudoku | Longest Consecutive Sequence | Valid Palindrome
"""

from collections import defaultdict
from typing import List


# ============================================================
# 1. VALID SUDOKU (LC 36) — Medium
# ============================================================

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Track seen digits per row, column, and 3x3 box simultaneously.
        (r//3, c//3) maps any cell to one of the 9 boxes — clean trick
        to avoid manually defining box boundaries.
        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3, c//3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True


# ============================================================
# 2. LONGEST CONSECUTIVE SEQUENCE (LC 128) — Medium
# ============================================================

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Convert to a set for O(1) lookups. Only start counting from a
        sequence's true start (num-1 not in set), so each sequence is
        walked exactly once — keeps it O(N) overall.
        """
        numset = set(nums)
        longest = 0

        for num in numset:
            if (num - 1) not in numset:
                length = 0
                while (num + length) in numset:
                    length += 1
                longest = max(longest, length)
        return longest


# ============================================================
# 3. VALID PALINDROME (LC 125) — Easy | Two Pointers
# ============================================================

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        return (ord('A') <= ord(c) <= ord('Z') or
                ord('a') <= ord(c) <= ord('z') or
                ord('0') <= ord(c) <= ord('9'))