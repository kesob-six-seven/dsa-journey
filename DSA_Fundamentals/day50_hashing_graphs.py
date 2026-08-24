"""
Day 50 — Hashing (Usage & Custom Implementation) & Intro to Graphs

Covers:
1. Hash Usage — frequency counting with a built-in dict
2. Hash Implementation — custom HashMap from scratch using open
   addressing (linear probing) for collision resolution
3. Intro to Graphs — three representations:
   - Matrix (generic 2D grid)
   - Adjacency Matrix (graph connectivity as a 2D grid)
   - Adjacency List (GraphNode with neighbor references)
"""


# -------------------------------------------------
# 1. Hash Usage — Frequency Counting
# -------------------------------------------------
names = ["alice", "brad", "collin", "brad", "dylan", "kim"]

countMap = {}
for name in names:
    # If countMap does not contain name
    if name not in countMap:
        countMap[name] = 1
    else:
        countMap[name] += 1


# -------------------------------------------------
# 2. Hash Implementation — Custom HashMap (Open Addressing)
# -------------------------------------------------
class Pair:
    def __init__(self, key, val):
        self.key = key
        self.val = val


class HashMap:
    def __init__(self):
        self.size = 0
        self.capacity = 2
        self.map = [None, None]

    def hash(self, key):
        """Sum of char codes mod capacity — simple string hash function."""
        index = 0
        for c in key:
            index += ord(c)
        return index % self.capacity

    def get(self, key):
        """
        THEORY:
        Open addressing (linear probing): start at the hashed index
        and scan forward (wrapping via modulo) until we find the key
        or hit an empty slot (meaning the key isn't present).

        TC: O(1) average, O(N) worst case (many collisions)
        SC: O(1)
        """
        index = self.hash(key)

        while self.map[index] != None:
            if self.map[index].key == key:
                return self.map[index].val
            index += 1
            index = index % self.capacity
        return None

    def put(self, key, val):
        """
        THEORY:
        Linear probe to find an empty slot or an existing matching key
        to update. Triggers a rehash once load factor gets too high
        (here: size >= capacity // 2) to keep probe chains short.

        TC: O(1) average, O(N) worst case
        SC: O(1) amortized (O(N) during rehash)
        """
        index = self.hash(key)

        while True:
            if self.map[index] == None:
                self.map[index] = Pair(key, val)
                self.size += 1
                if self.size >= self.capacity // 2:
                    self.rehash()
                return
            elif self.map[index].key == key:
                self.map[index].val = val
                return

            index += 1
            index = index % self.capacity

    def remove(self, key):
        """
        NOTE (bug called out intentionally):
        Setting the slot to None creates a "hole" in the open-addressing
        chain. A subsequent get() may stop probing early at this hole
        and incorrectly report a key as missing, even if it exists
        further along the probe sequence. Proper fix requires tombstone
        markers instead of None.
        """
        if not self.get(key):
            return

        index = self.hash(key)
        while True:
            if self.map[index].key == key:
                self.map[index] = None
                self.size -= 1
                return
            index += 1
            index = index % self.capacity

    def rehash(self):
        """
        THEORY:
        Doubles capacity and reinserts every existing pair into the
        new larger table (indices change since capacity changed).

        TC: O(N) — re-put every element
        SC: O(N) — new table allocation
        """
        self.capacity = 2 * self.capacity
        newMap = []
        for i in range(self.capacity):
            newMap.append(None)

        oldMap = self.map
        self.map = newMap
        self.size = 0
        for pair in oldMap:
            if pair:
                self.put(pair.key, pair.val)

    def print(self):
        for pair in self.map:
            if pair:
                print(pair.key, pair.val)


# -------------------------------------------------
# 3. Intro to Graphs — Representations
# -------------------------------------------------

# Matrix (2D Grid) — generic grid, e.g. for maze/pathfinding problems
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Adjacency Matrix — adjMatrix[i][j] = 1 means an edge exists between
# node i and node j. O(V^2) space, O(1) edge lookup.
adjMatrix = [[0, 0, 0, 0],
             [1, 1, 0, 0],
             [0, 0, 0, 1],
             [0, 1, 0, 0]]


# Adjacency List — each node stores direct references to its neighbors.
# More space-efficient than an adjacency matrix for sparse graphs:
# O(V + E) space vs O(V^2).
class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []