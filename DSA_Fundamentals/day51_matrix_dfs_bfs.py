"""
Day 51 — Graphs: Matrix DFS & Matrix BFS

Covers:
1. Matrix DFS — count all valid paths from top-left to bottom-right
   using backtracking (explore + undo visited state)
2. Matrix BFS — find the shortest path from top-left to bottom-right
   using level-by-level exploration
"""

from collections import deque


# -------------------------------------------------
# 1. Matrix DFS — Count All Paths (Backtracking)
# -------------------------------------------------
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]


def dfs(grid, r, c, visit):
    """
    THEORY:
    Explore all 4 directions from (r, c). Backtracking pattern:
    mark the cell visited before recursing, then unmark it (visit.remove)
    after exploring all branches — this allows OTHER paths to reuse
    that cell, which is essential since we're counting ALL distinct
    paths, not just checking reachability.

    Base cases: out of bounds, already visited (in current path), or
    a wall (grid[r][c] == 1) -> 0 paths from here.
    Reaching bottom-right -> 1 valid path found.

    TC: O(4^(R*C)) worst case — exponential, explores all path
        combinations (no memoization since paths must be distinct)
    SC: O(R*C) — recursion depth + visit set
    """
    ROWS, COLS = len(grid), len(grid[0])
    if (min(r, c) < 0 or
        r == ROWS or c == COLS or
        (r, c) in visit or grid[r][c] == 1):
        return 0
    if r == ROWS - 1 and c == COLS - 1:
        return 1

    visit.add((r, c))

    count = 0
    count += dfs(grid, r + 1, c, visit)
    count += dfs(grid, r - 1, c, visit)
    count += dfs(grid, r, c + 1, visit)
    count += dfs(grid, r, c - 1, visit)

    visit.remove((r, c))
    return count


# -------------------------------------------------
# 2. Matrix BFS — Shortest Path
# -------------------------------------------------
def bfs(grid):
    """
    THEORY:
    BFS explores the grid level-by-level (ring by ring, outward from
    the start). Since every move has equal cost (1 step), the first
    time we reach the target, we've necessarily found the SHORTEST
    path — no backtracking or path-undoing needed here, since we
    only care about distance, not enumerating all paths.

    Unlike DFS, visited cells are never "unmarked" — once explored,
    a cell doesn't need revisiting because BFS guarantees the first
    visit is via the shortest route.

    TC: O(R*C) — each cell visited at most once
    SC: O(R*C) — queue + visited set
    """
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = deque()
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for i in range(len(queue)):
            r, c = queue.popleft()
            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or
                    r + dr == ROWS or c + dc == COLS or
                    (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1