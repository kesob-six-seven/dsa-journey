"""
Day 93 — NeetCode 150: Graphs
Rotting Oranges (LC 994) — Medium
"""

from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Multi-source BFS — start from all rotten oranges simultaneously.
        Each BFS level = 1 minute. Count fresh oranges, decrement as
        they rot. If any fresh remain after BFS, return -1.
        """
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        dirc = [[1,0],[-1,0],[0,1],[0,-1]]

        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirc:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or grid[nr][nc] != 1:
                        continue
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc))
            minutes += 1

        return minutes if fresh == 0 else -1