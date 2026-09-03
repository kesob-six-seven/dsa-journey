"""
Day 60 — NeetCode 150: Sliding Window
Best Time to Buy and Sell Stock | Longest Substring Without Repeating Characters
"""

from typing import List


# ============================================================
# 1. BEST TIME TO BUY AND SELL STOCK (LC 121) — Easy
# ============================================================

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        mux = 0

        while r < len(prices):
            if prices[r] > prices[l]:
                pro = prices[r] - prices[l]
                mux = max(pro, mux)
            else:
                l = r
            r += 1
        return mux


# ============================================================
# 2. LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS (LC 3) — Medium
# ============================================================

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window with a set tracking current window chars.
        When a duplicate is found, shrink from the left until it's gone,
        then expand right — window always stays duplicate-free.
        """
        l = 0
        setl = set()
        res = 0

        for r in range(len(s)):
            while s[r] in setl:
                setl.remove(s[l])
                l += 1
            setl.add(s[r])
            res = max(res, r - l + 1)
        return res