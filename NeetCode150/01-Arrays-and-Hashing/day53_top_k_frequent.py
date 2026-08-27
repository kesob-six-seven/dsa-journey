"""
Day 53 — NeetCode 150: Arrays & Hashing
Top K Frequent Elements (LC 347) — Medium
"""

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Instead of sorting by frequency (O(N log N)), we use bucket sort.
        Index of each bucket = frequency. Since no number can appear more
        than len(nums) times, we make len(nums)+1 buckets. Then we just
        walk buckets from highest frequency down until we have k results.
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items():
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res