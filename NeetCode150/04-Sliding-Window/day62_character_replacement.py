"""
Day 62 — NeetCode 150: Sliding Window
Longest Repeating Character Replacement (LC 424) — Medium
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Window is valid when (window size - most frequent char count) <= k,
        meaning we only need to replace that many chars to make all uniform.
        Track maxf as the highest frequency seen — if window becomes invalid
        shrink from the left.
        """
        count = {}
        res = 0
        l = 0
        maxf = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res