"""
=========================================================
TOPIC: ARRAY FUNDAMENTALS (NeetCode Beginners)
STATUS: COMPLETED
=========================================================
"""
from typing import List

class MaxConsecutiveOnes:
    """
    PROBLEM 1: Max Consecutive Ones
    
    THEORY & INTUITION:
    Maintain a running counter of 1s and a global maximum. 
    If you see a 1, increment the current count and update the max. 
    If you see a 0, reset the current count to 0.
    
    TC: O(N) - Single pass through the array.
    SC: O(1) - Only using two integer variables.
    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        current_count = 0
        
        for n in nums:
            if n == 1:
                current_count += 1
                max_count = max(max_count, current_count)
            else:
                current_count = 0
                
        return max_count

class RemoveElement:
    """
    PROBLEM 2: Remove Element
    
    THEORY & INTUITION:
    Use the Two-Pointer technique. 
    Pointer `i` iterates through the array. 
    Pointer `k` keeps track of the position where the next valid (non-target) 
    element should be placed.
    
    TC: O(N) - Single pass.
    SC: O(1) - Modifying the array in-place.
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

class ReplaceElements:
    """
    PROBLEM 3: Replace Elements With Greatest Element On Right Side
    
    THEORY & INTUITION:
    Instead of checking the right side for every element O(N^2), iterate backwards.
    Keep track of the maximum value seen so far from the right (`right_max`).
    Replace the current element with `right_max`, then update `right_max`.
    
    TC: O(N) - Single reverse pass.
    SC: O(1) - Modifying in-place.
    """
    def replaceElements(self, arr: List[int]) -> List[int]:
        right_max = -1  # The last element is always replaced by -1
        
        for i in range(len(arr) - 1, -1, -1):
            # Store the current element before overwriting it
            current = arr[i]
            
            # Replace current with the greatest element on its right
            arr[i] = right_max
            
            # Update the greatest element seen so far
            right_max = max(right_max, current)
            
        return arr