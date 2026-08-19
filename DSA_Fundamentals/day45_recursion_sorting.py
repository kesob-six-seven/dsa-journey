"""
=========================================================
TOPIC: RECURSION & SORTING (NeetCode Beginners)
STATUS: COMPLETED
=========================================================
"""
from typing import List

# ==========================================
# 1. RECURSION
# ==========================================
class RecursionBasics:
    """
    Factorial: n! = n * (n-1)!
    TC: O(N), SC: O(N) due to the call stack.
    """
    def factorial(self, n: int) -> int:
        if n <= 1:
            return 1
        return n * self.factorial(n - 1)

    """
    Fibonacci: F(n) = F(n-1) + F(n-2)
    TC: O(2^N) - Extremely slow without memoization.
    SC: O(N) - Max depth of the call stack.
    """
    def fibonacci(self, n: int) -> int:
        if n <= 1:
            return n
        return self.fibonacci(n - 1) + self.fibonacci(n - 2)

# ==========================================
# 2. SORTING ALGORITHMS
# ==========================================
class SortingAlgorithms:
    """
    Insertion Sort: Builds the sorted array one element at a time.
    TC: O(N^2) worst/average, O(N) best. SC: O(1).
    """
    def insertionSort(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            j = i - 1
            while j >= 0 and arr[j + 1] < arr[j]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                j -= 1
        return arr

    """
    Merge Sort: Divide and Conquer. Splits array in half, recursively sorts, and merges.
    TC: O(N \log N) always. SC: O(N).
    """
    def mergeSort(self, arr: List[int], s: int, e: int) -> List[int]:
        if e - s + 1 <= 1:
            return arr

        m = (s + e) // 2
        self.mergeSort(arr, s, m)
        self.mergeSort(arr, m + 1, e)
        self.merge(arr, s, m, e)
        return arr

    def merge(self, arr: List[int], s: int, m: int, e: int):
        L = arr[s:m + 1]
        R = arr[m + 1:e + 1]
        i = j = 0
        k = s
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    """
    Quick Sort: Picks a pivot, places smaller elements left and larger right.
    TC: O(N \log N) average, O(N^2) worst case. SC: O(\log N) recursion stack.
    """
    def quickSort(self, arr: List[int], s: int, e: int) -> List[int]:
        if e - s + 1 <= 1:
            return arr

        pivot = arr[e]
        left = s  # Pointer for elements smaller than pivot

        for i in range(s, e):
            if arr[i] < pivot:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1

        # Move pivot to its correct position
        arr[left], arr[e] = arr[e], arr[left]

        self.quickSort(arr, s, left - 1)
        self.quickSort(arr, left + 1, e)
        return arr

    """
    Bucket Sort: Excellent for sorting frequencies or bounded integer ranges.
    TC: O(N), SC: O(N).
    """
    def bucketSort(self, arr: List[int]) -> List[int]:
        # Assuming values are in the range 0 to 2 (e.g., [0, 1, 1, 2, 0])
        counts = [0, 0, 0] 
        for n in arr:
            counts[n] += 1

        i = 0
        for n in range(len(counts)):
            for j in range(counts[n]):
                arr[i] = n
                i += 1
        return arr