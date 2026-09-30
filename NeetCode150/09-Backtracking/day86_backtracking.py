"""
Day 86 — NeetCode 150: Backtracking
Subsets | Combination Sum | Combination Sum II | Permutations
"""

from typing import List


# ============================================================
# 1. SUBSETS (LC 78) — Medium
# ============================================================

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        At each index, two choices — include or exclude. DFS explores
        both branches, building subsets bottom-up via backtracking.
        """
        res = []

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()
            dfs(i + 1, subset)

        dfs(0, [])
        return res


# ============================================================
# 2. COMBINATION SUM (LC 39) — Medium
# ============================================================

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Can reuse same element — pass same index i on include branch.
        Move to i+1 on exclude to avoid duplicate combos.
        """
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if i >= len(candidates) or total > target:
                return
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res


# ============================================================
# 3. COMBINATION SUM II (LC 40) — Medium
# ============================================================

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Sort first — skip duplicates at the same tree level to avoid
        duplicate combinations. Each element used only once (i+1).
        """
        candidates.sort()
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if total > target or i >= len(candidates):
                return
            curr.append(candidates[i])
            dfs(i + 1, curr, total + candidates[i])
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, curr, total)

        dfs(0, [], 0)
        return res


# ============================================================
# 4. PERMUTATIONS (LC 46) — Medium
# ============================================================

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        At each step pick any unused number. Use a set to track what's
        already in the current permutation — backtrack after each pick.
        """
        res = []

        def dfs(perm):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            for n in nums:
                if n not in perm:
                    perm.append(n)
                    dfs(perm)
                    perm.pop()

        dfs([])
        return res