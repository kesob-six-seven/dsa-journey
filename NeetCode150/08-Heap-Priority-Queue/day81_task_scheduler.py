"""
Day 81 — NeetCode 150: Heap / Priority Queue
Task Scheduler (LC 621) — Medium
"""

import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Max heap processes the most frequent task first each cycle.
        Cooldown queue holds (count, available_time) — tasks re-enter
        the heap only when their cooldown expires. Time ticks each step
        whether we process a task or idle.
        """
        count = Counter(tasks)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        queue = deque()  # (count, available_at)

        while maxHeap or queue:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1  # decrement (negated)
                if cnt:
                    queue.append((cnt, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])

        return time