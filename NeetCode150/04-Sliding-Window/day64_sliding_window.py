"""
Day 64 — NeetCode 150: Sliding Window Complete
Permutation in String | Minimum Window Substring | Sliding Window Maximum
"""

from collections import deque


# ============================================================
# 1. PERMUTATION IN STRING (LC 567) — Medium
# ============================================================

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Fixed-size window of len(s1) slides over s2. Track a `matches`
        counter across 26 chars — update only the incoming and outgoing
        character each slide instead of recomputing the whole window.
        """
        if len(s1) > len(s2):
            return False

        s1Count, s2Count = [0] * 26, [0] * 26
        for i in range(len(s1)):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        matches = sum(1 for i in range(26) if s1Count[i] == s2Count[i])
        l = 0

        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord('a')
            s2Count[index] += 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                matches -= 1

            index = ord(s2[l]) - ord('a')
            s2Count[index] -= 1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                matches -= 1
            l += 1

        return matches == 26


# ============================================================
# 2. MINIMUM WINDOW SUBSTRING (LC 76) — Hard
# ============================================================

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Expand right until all chars in t are satisfied (have == need),
        then shrink from left to minimize. Record smallest valid window.
        """
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l: r + 1] if resLen != float("infinity") else ""


# ============================================================
# 3. SLIDING WINDOW MAXIMUM (LC 239) — Hard
# ============================================================

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Monotonic decreasing deque stores indices. Front is always the
        max of the current window. Before adding a new element, pop from
        the back anything smaller — they can never be the max while the
        new element is in the window. Pop from front if it's out of range.
        """
        output = []
        q = deque()
        l = 0

        for r in range(len(nums)):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if q[0] < l:
                q.popleft()

            if r + 1 >= k:
                output.append(nums[q[0]])
                l += 1

        return output