"""
Day 59 — NeetCode 150: Stack
Valid Parentheses | Min Stack | Trapping Rain Water
"""

from typing import List


# ============================================================
# 1. VALID PARENTHESES (LC 20) — Easy
# ============================================================

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        cto = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in cto:
                if stack and stack[-1] == cto[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack


# ============================================================
# 2. MIN STACK (LC 155) — Medium
# ============================================================

class MinStack:
    """
    A second parallel stack tracks the current minimum at every level.
    When we pop the main stack, we pop the min stack too — so getMin()
    always reflects the minimum of whatever's currently in the stack.
    """

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        val = min(value, self.minstack[-1] if self.minstack else value)
        self.minstack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]


# ============================================================
# 3. TRAPPING RAIN WATER (LC 42) — Hard
# ============================================================

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Water trapped at any index = min(leftMax, rightMax) - height[i].
        Two pointers let us compute this in one pass — always process
        the side with the smaller max since that's the bottleneck.
        """
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res