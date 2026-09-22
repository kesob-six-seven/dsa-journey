"""
Day 78 — NeetCode 150: Heap / Priority Queue
Kth Largest Element in a Stream | Last Stone Weight
"""

import heapq
from typing import List


# ============================================================
# 1. KTH LARGEST ELEMENT IN A STREAM (LC 703) — Easy
# ============================================================

class KthLargest:
    """
    Min heap of size k — the root is always the kth largest element.
    When heap exceeds size k, pop the smallest. Whatever's at the
    top after adding is the kth largest by definition.
    """

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


# ============================================================
# 2. LAST STONE WEIGHT (LC 1046) — Easy
# ============================================================

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Python only has min heap — negate values to simulate max heap.
        Smash the two heaviest stones each round until one or zero remain.
        """
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            first = heapq.heappop(heap)
            second = heapq.heappop(heap)
            if first != second:
                heapq.heappush(heap, first - second)

        return -heap[0] if heap else 0