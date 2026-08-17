"""
=========================================================
TOPIC: STACK FUNDAMENTALS (NeetCode Beginners)
STATUS: COMPLETED
=========================================================
"""

class ValidParentheses:
    """
    PROBLEM 1: Valid Parentheses
    
    THEORY & INTUITION:
    We use a Stack to keep track of opening brackets. 
    A Hash Map keeps our code clean by mapping closing brackets to their 
    corresponding opening brackets. 
    If we see an open bracket, push it. If we see a closed bracket, check 
    if it matches the top of the stack.
    
    TC: O(N) - We traverse the string exactly once.
    SC: O(N) - In the worst case (all open brackets), the stack holds N elements.
    """
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                if stack and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
                
        return not stack


class MinStack:
    """
    PROBLEM 2: Min Stack
    
    THEORY & INTUITION:
    We need to retrieve the minimum element in O(1) time. 
    A standard stack only gives us O(1) for push, pop, and top. 
    To solve this, we use TWO stacks:
    1. A main stack to keep the actual values.
    2. A min_stack to keep track of the minimum value at each level of the main stack.
    
    TC: O(1) - For all operations (push, pop, top, getMin).
    SC: O(N) - For storing elements in the two stacks.
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if self.min_stack:
            val = min(val, self.min_stack[-1])
            
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]