"""
Day 56 — NeetCode 150: Arrays & Hashing
Product of Array Except Self (LC 238) — Medium
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Two passes instead of computing products with division (which
        breaks when zeros are involved). First pass fills each index
        with the product of everything to its LEFT. Second pass
        multiplies in the product of everything to its RIGHT.
        Result at each index = left product * right product = everything
        except self, all in O(1) extra space.
        """
        res = [1] * len(nums)
        prefix = 1

        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res