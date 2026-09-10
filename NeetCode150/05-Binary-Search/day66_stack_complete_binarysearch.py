"""
Day 66 — NeetCode 150: Stack Complete + Binary Search Begins
Car Fleet | Largest Rectangle in Histogram | Binary Search | Search a 2D Matrix
"""

from typing import List


# ============================================================
# 1. CAR FLEET (LC 853) — Medium
# ============================================================

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        Sort cars by position descending (closest to target first).
        Calculate time each car needs to reach target. If a car behind
        takes <= time than the car ahead, it catches up and merges into
        the same fleet — don't count it separately.
        Stack top always holds the slowest (leading) fleet's time.
        """
        pairs = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in pairs:
            time = (target - pos) / spd
            stack.append(time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)


# ============================================================
# 2. LARGEST RECTANGLE IN HISTOGRAM (LC 84) — Hard
# ============================================================

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        Monotonic increasing stack stores (index, height) pairs.
        When a shorter bar is found, pop taller bars and extend their
        width back to where they were first "blocked" — that's the
        largest rectangle they can form.
        """
        maxArea = 0
        stack = []  # (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx
            stack.append((start, h))

        for idx, height in stack:
            maxArea = max(maxArea, height * (len(heights) - idx))

        return maxArea


# ============================================================
# 3. BINARY SEARCH (LC 704) — Easy
# ============================================================

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return -1


# ============================================================
# 4. SEARCH A 2D MATRIX (LC 74) — Medium
# ============================================================

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Treat the matrix as a flattened sorted array. Map mid index back
        to (row, col) using divmod — binary search works identically.
        """
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1

        while l <= r:
            mid = (l + r) // 2
            row, col = divmod(mid, cols)
            val = matrix[row][col]

            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1

        return False