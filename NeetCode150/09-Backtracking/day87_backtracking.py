"""
Day 87 — NeetCode 150: Backtracking
Subsets II | Generate Parentheses | Word Search | Palindrome Partitioning
"""

from typing import List


# ============================================================
# 1. SUBSETS II (LC 90) — Medium
# ============================================================

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Sort first. Skip duplicates at the same tree level — same trick
        as Combination Sum II to avoid duplicate subsets.
        """
        nums.sort()
        res = []

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, subset)

        dfs(0, [])
        return res


# ============================================================
# 2. GENERATE PARENTHESES (LC 22) — Medium
# ============================================================

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Only add open bracket if open < n.
        Only add close bracket if close < open.
        When open == close == n, valid combo found.
        """
        res = []

        def dfs(open, close, curr):
            if open == close == n:
                res.append(curr)
                return
            if open < n:
                dfs(open + 1, close, curr + "(")
            if close < open:
                dfs(open, close + 1, curr + ")")

        dfs(0, 0, "")
        return res


# ============================================================
# 3. WORD SEARCH (LC 79) — Medium
# ============================================================

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        DFS from every cell that matches word[0]. Mark visited cells
        with a placeholder to avoid reuse, restore after backtracking.
        """
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            tmp = board[r][c]
            board[r][c] = "#"
            found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            board[r][c] = tmp
            return found

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        return False


# ============================================================
# 4. PALINDROME PARTITIONING (LC 131) — Medium
# ============================================================

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        At each index, try every substring starting here — if it's a
        palindrome, add it and recurse on the remainder. Backtrack after.
        """
        res = []

        def dfs(i, curr):
            if i == len(s):
                res.append(curr[:])
                return
            for j in range(i, len(s)):
                if isPalin(s, i, j):
                    curr.append(s[i:j+1])
                    dfs(j + 1, curr)
                    curr.pop()

        def isPalin(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        dfs(0, [])
        return res