"""
Day 99 — NeetCode 150: Graphs
Redundant Connection | Word Ladder
"""

from typing import List
from collections import deque, defaultdict


# ============================================================
# 1. REDUNDANT CONNECTION (LC 684) — Medium
# ============================================================

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Union-Find — process edges one by one. The first edge where
        both nodes already share the same root creates a cycle — that's
        the redundant connection to remove.
        """
        parent = list(range(len(edges) + 1))
        rank = [1] * (len(edges) + 1)

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

        for u, v in edges:
            if not union(u, v):
                return [u, v]


# ============================================================
# 2. WORD LADDER (LC 127) — Hard
# ============================================================

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        BFS — each level = one transformation. Pre-build a pattern map
        (*ot, h*t, ho*) -> [words] for O(1) neighbor lookup instead of
        checking every word in the list each step.
        """
        if endWord not in wordList:
            return 0

        neighbors = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbors[pattern].append(word)

        visit = set([beginWord])
        queue = deque([beginWord])
        res = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return res
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            queue.append(neighbor)
            res += 1

        return 0