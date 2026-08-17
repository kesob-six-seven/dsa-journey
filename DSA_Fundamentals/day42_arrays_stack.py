"""
=========================================================
TOPIC: ARRAY & STACK FUNDAMENTALS (NeetCode Beginners)
STATUS: COMPLETED
=========================================================
"""
from typing import List

class ConcatenationOfArray:
    """
    PROBLEM 1: Concatenation of Array
    
    THEORY & INTUITION:
    We need an array that is basically the original array appended to itself.
    In Python, list concatenation makes this extremely simple and efficient 
    using the `+` operator, which creates a new list behind the scenes.
    
    TC: O(N) - Creating a new array of size 2N.
    SC: O(N) - Space needed for the new array.
    """
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums + nums

class BaseballGame:
    """
    PROBLEM 2: Baseball Game
    
    THEORY & INTUITION:
    This is a classic Stack problem. We process a stream of operations where 
    some operations require us to look back at previous scores or remove them entirely.
    A Stack perfectly models this Last-In-First-Out (LIFO) requirement.
    
    TC: O(N) - Single pass through the operations list.
    SC: O(N) - Storing up to N valid scores in the stack.
    """
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        
        for op in operations:
            if op == "+":
                # Add the top two scores and push the result
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                # Double the top score and push the result
                stack.append(stack[-1] * 2)
            elif op == "C":
                # Invalidate the previous score by popping it off
                stack.pop()
            else:
                # It's a standard integer string, cast and push
                stack.append(int(op))
                
        return sum(stack)