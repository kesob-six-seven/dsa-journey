"""
Day 91 — NeetCode 150: Graphs
Number of Islands (LC 200) — Medium
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dir =[1,0],[-1,0],[0,1],[0,-1]
        rows, cols=len(grid), len(grid[0])

        islands=0
        def bfs( r, c):
            q= deque()
            grid[r][c]="0"
            q.append((r,c))

            while q:
                row, col=q.popleft()
                for dr, dc in dir :
                    nr =row+dr
                    nc=col+dc
                    #cols col shit fried me up he he han 
                    if (nr<0 or nc<0 or nr>=rows or nc>=cols or grid[nr][nc]=="0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc]="0"


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    bfs(r,c)
                    islands+=1
        return islands 
