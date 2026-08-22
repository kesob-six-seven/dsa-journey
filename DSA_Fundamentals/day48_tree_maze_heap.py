"""
Day 48 — Tree Maze (Recursive Backtracking) & Heap / Priority Queue (Array-Based Min-Heap)

Covers:
1. Tree Maze — treat a binary tree as a maze where a 0-value node is
   a "wall" (blocked path). Find if any root-to-leaf path exists
   avoiding walls, and optionally reconstruct that path.
2. Min Heap — array-based implementation using index math:
   - leftChild(i)  = heap[2*i]
   - rightChild(i) = heap[2*i + 1]
   - parent(i)     = heap[i // 2]
   Index 0 is a dummy/reserved slot so root sits at index 1.
"""


# -------------------------------------------------
# 1. Tree Maze
# -------------------------------------------------
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def canReachLeaf(root):
    """
    THEORY:
    DFS down the tree. A node with val == 0 is a blocked wall —
    stop exploring that branch. If we hit a leaf without ever
    passing through a wall, a valid path exists.

    TC: O(N) worst case — visit every node
    SC: O(H) recursion stack, H = tree height
    """
    if not root or root.val == 0:
        return False

    if not root.left and not root.right:
        return True
    if canReachLeaf(root.left):
        return True
    if canReachLeaf(root.right):
        return True
    return False


def leafPath(root, path):
    """
    THEORY:
    Same maze logic as canReachLeaf, but with backtracking to
    reconstruct the actual path. Append the current node's value
    speculatively; if neither subtree leads to a valid leaf, pop
    it off before returning False (undo the choice).

    TC: O(N) worst case
    SC: O(H) recursion stack + O(H) path list
    """
    if not root or root.val == 0:
        return False
    path.append(root.val)

    if not root.left and not root.right:
        return True
    if leafPath(root.left, path):
        return True
    if leafPath(root.right, path):
        return True
    path.pop()
    return False


# -------------------------------------------------
# 2. Min Heap — Array-Based Implementation
# -------------------------------------------------
# leftChild of i  = heap[2 * i]
# rightChild of i = heap[(2 * i) + 1]
# parent of i     = heap[i // 2]
class Heap:
    def __init__(self):
        self.heap = [0]  # index 0 unused/dummy, root lives at index 1

    def push(self, val):
        """
        THEORY:
        Append to the end (maintains complete tree shape), then
        percolate up: swap with parent while smaller than parent.

        TC: O(log N) — height of a complete binary tree
        SC: O(1)
        """
        self.heap.append(val)
        i = len(self.heap) - 1

        # Percolate up
        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2

    def pop(self):
        """
        THEORY:
        Root is always the min. Move the last element to the root
        (maintains complete shape), then percolate down: repeatedly
        swap with the smaller child until heap order is restored.

        TC: O(log N)
        SC: O(1)
        """
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()

        res = self.heap[1]
        # Move last value to root
        self.heap[1] = self.heap.pop()
        i = 1
        # Percolate down
        while 2 * i < len(self.heap):
            if (2 * i + 1 < len(self.heap) and
                self.heap[2 * i + 1] < self.heap[2 * i] and
                self.heap[i] > self.heap[2 * i + 1]):
                # Swap right child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i + 1]
                self.heap[2 * i + 1] = tmp
                i = 2 * i + 1
            elif self.heap[i] > self.heap[2 * i]:
                # Swap left child
                tmp = self.heap[i]
                self.heap[i] = self.heap[2 * i]
                self.heap[2 * i] = tmp
                i = 2 * i
            else:
                break
        return res

    def top(self):
        if len(self.heap) > 1:
            return self.heap[1]
        return None

    def heapify(self, arr):
        """
        THEORY:
        Convert an arbitrary array into a valid min-heap in-place.
        Start from the last non-leaf node (len // 2) and percolate
        each node down to its correct position, working backwards
        to the root. This bottom-up approach is O(N) overall
        (not O(N log N)) because most nodes are near the bottom
        and require little to no work.

        TC: O(N)
        SC: O(1) extra (in-place, ignoring input array)
        """
        # 0-th position is moved to the end
        arr.append(arr[0])

        self.heap = arr
        cur = (len(self.heap) - 1) // 2
        while cur > 0:
            # Percolate down
            i = cur
            while 2 * i < len(self.heap):
                if (2 * i + 1 < len(self.heap) and
                    self.heap[2 * i + 1] < self.heap[2 * i] and
                    self.heap[i] > self.heap[2 * i + 1]):
                    # Swap right child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = tmp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    # Swap left child
                    tmp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = tmp
                    i = 2 * i
                else:
                    break
            cur -= 1