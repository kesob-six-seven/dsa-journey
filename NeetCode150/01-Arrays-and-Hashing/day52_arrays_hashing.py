"""
Day 52 — NeetCode 150: Arrays & Hashing (Problems 1-4)
Contains Duplicate | Valid Anagram | Two Sum | Group Anagrams
"""

from collections import defaultdict


# ============================================================
# 1. CONTAINS DUPLICATE (LC 217) — Easy
# ============================================================

def hasDuplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False


# ============================================================
# 2. VALID ANAGRAM (LC 242) — Easy
# ============================================================

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for c in t:
        count[c] = count.get(c, 0) - 1
        if count[c] < 0:
            return False
    return True


# ============================================================
# 3. TWO SUM (LC 1) — Easy
# ============================================================

def twoSum(nums, target):
    """
    THEORY & INTUITION:
    As we iterate, we store each number and its index in a hash map.
    For every new number, we check if its complement (target - num)
    already exists in the map. If yes, we found our pair in O(1) lookup
    instead of scanning the whole array again (which would be O(N²)).

    TC: O(N)  SC: O(N)
    """
    seen = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in seen:
            return [seen[diff], i]
        seen[n] = i


# ============================================================
# 4. GROUP ANAGRAMS (LC 49) — Medium
# ============================================================

def groupAnagrams(strs):
    """
    THEORY & INTUITION:
    Two words are anagrams if they have the exact same character
    frequencies. Instead of sorting (O(K log K) per word), we build
    a frequency tuple of 26 counts as the key — one slot per letter.
    All anagrams map to the same key, so they naturally group together
    in the hash map.

    TC: O(N * K)  SC: O(N * K)  where K = avg word length
    """
    groups = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        groups[tuple(count)].append(s)
    return list(groups.values())