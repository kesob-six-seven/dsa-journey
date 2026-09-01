"""
Day 58 — NeetCode 150: Two Pointers
Two Sum II | 3Sum | Container With Most Water
"""

from typing import List


# ============================================================
# 1. TWO SUM II (LC 167) — Medium
# ============================================================

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            s = numbers[l] + numbers[r]
            if s > target:
                r -= 1
            elif s < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []


# ============================================================
# 2. 3SUM (LC 15) — Medium
# ============================================================

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Sort first, then fix one number and run two pointers on the rest.
        Skipping duplicates at both the outer loop and inner pointers
        ensures no duplicate triplets in the result.
        """
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res


# ============================================================
# 3. CONTAINER WITH MOST WATER (LC 11) — Medium
# ============================================================

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Always move the shorter pointer inward — keeping the taller one
        can only help since width is already shrinking.
        """
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res