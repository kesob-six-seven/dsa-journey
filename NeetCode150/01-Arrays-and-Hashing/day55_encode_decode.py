"""
Day 55 — NeetCode 150: Arrays & Hashing
Encode and Decode Strings (LC 271) — Medium
"""

from typing import List


class Solution:
    def encode(self, strs: List[str]) -> str:
        """
        Prefix each string with its length and a '#' delimiter.
        e.g. ["neet","code"] -> "4#neet4#code"
        This way decode always knows exactly how many chars to read,
        even if the string itself contains '#' or digits.
        """
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res