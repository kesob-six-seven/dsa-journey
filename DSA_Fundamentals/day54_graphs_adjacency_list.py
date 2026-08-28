"""
Day 54 — DSA Fundamentals: Graphs — Adjacency List, DFS & BFS
NeetCode DSA for Beginners | Module 31
"""

from collections import deque


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


# Build adjacency list from directed edges
edges = [["A", "B"], ["B", "C"], ["B", "E"], ["C", "E"], ["E", "D"]]

adjList = {}
for src, dst in edges:
    if src not in adjList:
        adjList[src] = []
    if dst not in adjList:
        adjList[dst] = []
    adjList[src].append(dst)


def dfs(node, target, adjList, visit):
    """
    Backtracking DFS — counts ALL distinct paths from node to target.
    We mark a node visited before recursing and unmark it after so
    other paths can reuse it (backtracking pattern).
    """
    if node in visit:
        return 0
    if node == target:
        return 1

    count = 0
    visit.add(node)
    for neighbor in adjList[node]:
        count += dfs(neighbor, target, adjList, visit)
    visit.remove(node)
    return count


def bfs(node, target, adjList):
    """
    BFS guarantees shortest path because it explores level by level.
    Each level = one edge away, so the moment we hit target, `length`
    is the minimum number of edges to get there.
    """
    length = 0
    visit = set()
    visit.add(node)
    queue = deque([node])

    while queue:
        for i in range(len(queue)):
            curr = queue.popleft()
            if curr == target:
                return length
            for neighbor in adjList[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        length += 1
    return length