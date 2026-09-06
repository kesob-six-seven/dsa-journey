"""
Day 63 — NeetCode 150: Sliding Window
Permutation in String | Minimum Window Substring
"""


# ============================================================
# 1. PERMUTATION IN STRING (LC 567) — Medium
# ============================================================

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Fixed-size window of len(s1) slides over s2. Instead of
        recomputing frequency counts each slide, we track a `matches`
        counter (how many of 26 chars have equal counts in both windows).
        Each slide we adjust only the incoming and outgoing character,
        updating matches accordingly — O(1) per step.
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
        Expand right until we have all required chars (have == need),
        then shrink from the left to minimize the window — recording
        the smallest valid window seen. `have` increments only when a
        char's window count exactly meets its requirement in t.
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