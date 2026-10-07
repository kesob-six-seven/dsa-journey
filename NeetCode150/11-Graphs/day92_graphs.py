"""
Day 92 — NeetCode 150: Graphs
Max Area of Island | Clone Graph
"""

from typing import Optional
from collections import deque


# Definition for a Node
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


# ============================================================
# 1. MAX AREA OF ISLAND (LC 695) — Medium
# ============================================================

def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
    dirc = [[1,0],[-1,0],[0,-1],[0,1]]
    res = 0
    rows, cols = len(grid), len(grid[0])

    def bfs(r, c):
        q = deque()
        grid[r][c] = 0
        area = 1
        q.append((r, c))
        while q:
            row, col = q.popleft()
            for dr, dc in dirc:
                nr = row + dr
                nc = col + dc
                if nr < 0 or nr >= rows or nc >= cols or nc < 0 or grid[nr][nc] != 1:
                    continue
                q.append((nr, nc))
                grid[nr][nc] = 0
                area += 1
        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                res = max(res, bfs(r, c))
    return res

# ============================================================
# 2. CLONE GRAPH (LC 133) — Medium
# ============================================================

class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        """
        Hash map old -> new node. BFS visits every node once —
        for each node, create its clone and clone all its neighbors.
        Map prevents revisiting and handles cycles.
        """
        if not node:
            return None

        oldToNew = {}
        queue = deque([node])
        oldToNew[node] = Node(node.val)

        while queue:
            curr = queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in oldToNew:
                    oldToNew[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                oldToNew[curr].neighbors.append(oldToNew[neighbor])

        return oldToNew[node]