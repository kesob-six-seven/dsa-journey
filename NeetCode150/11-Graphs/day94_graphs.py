"""
Day 94 — NeetCode 150: Graphs
Walls and Gates (LC 286) — Medium
"""

from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Multi-source BFS from all gates simultaneously — same pattern
        as Rotting Oranges. Distance fills outward from every gate at
        once, guaranteeing each room gets the shortest distance.
        """
        INF = 2147483647
        rows, cols = len(rooms), len(rooms[0])
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    queue.append((r, c))

        dirc = [[1,0],[-1,0],[0,1],[0,-1]]
        dist = 0

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in dirc:
                    nr, nc = r + dr, c + dc
                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols or rooms[nr][nc] != INF:
                        continue
                    rooms[nr][nc] = rooms[r][c] + 1
                    queue.append((nr, nc))