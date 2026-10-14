"""
Day 98 — NeetCode 150: Graphs
Graph Valid Tree | Number of Connected Components in Undirected Graph
"""

from typing import List


# ============================================================
# 1. GRAPH VALID TREE (LC 261) — Medium
# ============================================================

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        A valid tree has exactly n-1 edges and no cycles.
        Union-Find: merge components via edges. If two nodes already
        share the same root before merging, a cycle exists — return False.
        Valid tree iff all nodes end up in one component.
        """
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            rank[px] += rank[py]
            return True

        if len(edges) != n - 1:
            return False

        for u, v in edges:
            if not union(u, v):
                return False

        return True


# ============================================================
# 2. NUMBER OF CONNECTED COMPONENTS (LC 323) — Medium
# ============================================================

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        Union-Find — start with n components. Each successful union
        reduces count by 1.
        """
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return 0
            if rank[px] < rank[py]:
                px, py = py, px
            parent[py] = px
            rank[px] += rank[py]
            return 1

        components = n
        for u, v in edges:
            components -= union(u, v)

        return components