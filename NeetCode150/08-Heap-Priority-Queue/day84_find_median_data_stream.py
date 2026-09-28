"""
Day 84 — NeetCode 150: Heap / Priority Queue Complete
Find Median from Data Stream (LC 295) — Hard
"""

import heapq


class MedianFinder:
    """
    Two heaps — max heap (small) for lower half, min heap (large) for
    upper half. Balance them so they differ by at most 1 in size.
    Median is either the top of the larger heap or average of both tops.
    """

    def __init__(self):
        self.small = []  # max heap (negated)
        self.large = []  # min heap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        # ensure every element in small <= every element in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # balance sizes
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2.0