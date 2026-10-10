"""
Day 95 — NeetCode 150: Graphs
Pacific Atlantic Water Flow (LC 417) — Medium
"""

from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Reverse thinking — instead of flowing water down from each cell,
        BFS upward from both ocean borders simultaneously. A cell that's
        reachable from both oceans is a valid answer.
        Pacific touches top/left borders, Atlantic touches bottom/right.
        """
        rows, cols = len(heights), len(heights[0])
        pac, atl = deque(), deque()
        pac_visit, atl_visit = set(), set()

        for c in range(cols):
            pac.append((0, c))
            atl.append((rows - 1, c))
            pac_visit.add((0, c))
            atl_visit.add((rows - 1, c))

        for r in range(rows):
            pac.append((r, 0))
            atl.append((r, cols - 1))
            pac_visit.add((r, 0))
            atl_visit.add((r, cols - 1))

        def bfs(queue, visit):
            dirc = [[1,0],[-1,0],[0,1],[0,-1]]
            while queue:
                r, c = queue.popleft()
                for dr, dc in dirc:
                    nr, nc = r + dr, c + dc
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or
                            (nr, nc) in visit or heights[nr][nc] < heights[r][c]):
                        continue
                    visit.add((nr, nc))
                    queue.append((nr, nc))

        bfs(pac, pac_visit)
        bfs(atl, atl_visit)

        return [[r, c] for r in range(rows) for c in range(cols)
                if (r, c) in pac_visit and (r, c) in atl_visit]