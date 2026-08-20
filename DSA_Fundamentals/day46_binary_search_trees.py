"""
Day 46 — DSA Fundamentals: Binary Search & Trees
NeetCode DSA for Beginners | Module 14-17: Search Array, Search Range,
Binary Tree, Binary Search Tree
"""


# ============================================================
# MODULE 14: BINARY SEARCH ON AN ARRAY
# ============================================================

def binary_search(arr, target):
    """
    THEORY & INTUITION:
    Binary Search works on a SORTED array by repeatedly cutting the
    search space in half instead of scanning element by element.

    We keep two pointers, L (left) and R (right), marking the current
    window we still need to check. At each step we look at the middle
    element:
        - If target > arr[mid]  -> target must be in the RIGHT half,
                                    so move L to mid + 1
        - If target < arr[mid]  -> target must be in the LEFT half,
                                    so move R to mid - 1
        - Otherwise              -> arr[mid] IS the target, return its index

    Every iteration throws away half the remaining elements, which is
    what gives Binary Search its logarithmic speed over a plain linear
    scan.

    Time Complexity  (TC): O(log N) — search space halves each iteration.
    Space Complexity (SC): O(1) — only two pointers used, no extra memory.
    """
    L, R = 0, len(arr) - 1

    while L <= R:
        mid = (L + R) // 2

        if target > arr[mid]:
            L = mid + 1
        elif target < arr[mid]:
            R = mid - 1
        else:
            return mid

    return -1  # target not found


# ============================================================
# MODULE 15: BINARY SEARCH ON A RANGE OF VALUES (SEARCH SPACE)
# ============================================================

def binary_search_range(low, high):
    """
    THEORY & INTUITION:
    Binary Search doesn't only work on arrays — it works on ANY sorted
    "search space" where you can ask "is this candidate too big, too
    small, or correct?" and get a consistent answer. Here the search
    space is just the range of numbers [low, high], with no actual
    array in memory.

    Instead of comparing against arr[mid], we call a helper function
    isCorrect(mid) that tells us:
        - 1  -> mid is too big    -> search the LEFT half  (high = mid - 1)
        - -1 -> mid is too small  -> search the RIGHT half (low = mid + 1)
        - 0  -> mid is exactly right -> return it

    This pattern generalizes Binary Search from "search a sorted array"
    to "binary search on the answer" — a technique used heavily in
    optimization-style interview problems (e.g. minimize/maximize some
    value subject to a condition).

    Time Complexity  (TC): O(log(high - low)) — range halves each iteration.
    Space Complexity (SC): O(1) — only two pointers used, no extra memory.
    """
    while low <= high:
        mid = (low + high) // 2

        if is_correct(mid) > 0:
            high = mid - 1
        elif is_correct(mid) < 0:
            low = mid + 1
        else:
            return mid

    return -1


def is_correct(n):
    """
    THEORY & INTUITION:
    A stand-in "oracle" function representing whatever condition you're
    binary searching for. Here it simply checks n against a hardcoded
    target (10), but in real problems this could be any monotonic
    check (e.g. "can I finish the task in n days?").

    Returns 1 if n is too big, -1 if too small, 0 if exactly correct.

    Time Complexity  (TC): O(1) — constant-time comparison.
    Space Complexity (SC): O(1).
    """
    if n > 10:
        return 1
    elif n < 10:
        return -1
    else:
        return 0


# ============================================================
# MODULE 16: BINARY TREE — NODE STRUCTURE
# ============================================================

class TreeNode:
    """
    THEORY & INTUITION:
    The fundamental building block of a binary tree. Each node stores a
    value plus two pointers — left and right — pointing to its children.
    Unlike a Linked List node (which only has ONE next pointer), this
    branching structure is what lets a tree represent hierarchical data
    instead of a straight line.

    A node starts with no children (left = None, right = None); children
    get attached as the tree is built.

    Time Complexity  (TC): O(1) to construct a single node.
    Space Complexity (SC): O(1) per node (excluding children it points to).
    """

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# ============================================================
# MODULE 17: BINARY SEARCH TREE — SEARCH
# ============================================================

def search(root, target):
    """
    THEORY & INTUITION:
    Searching a Binary SEARCH Tree (BST) uses the same halving idea as
    Binary Search on an array, except the "halves" are already encoded
    into the tree's structure via its core invariant:
        - everything in root.left  is  <  root.val
        - everything in root.right is  >  root.val

    So at each node we compare target against root.val and immediately
    know which single subtree to recurse into — we never need to check
    the other half at all:
        - target > root.val  -> recurse into root.right
        - target < root.val  -> recurse into root.left
        - target == root.val -> found it, return True

    If we ever recurse into a None node, the target doesn't exist on
    that path, so we return False.

    Time Complexity  (TC): O(H) where H = tree height. O(log N) average
                            for a balanced tree, O(N) worst case if the
                            tree is skewed (degenerates to a linked list).
    Space Complexity (SC): O(H) — recursive call stack depth.
    """
    if not root:
        return False

    if target > root.val:
        return search(root.right, target)
    elif target < root.val:
        return search(root.left, target)
    else:
        return True


if __name__ == "__main__":
    # --- Binary Search on array ---
    arr = [1, 3, 3, 4, 5, 6, 7, 8]
    print(binary_search(arr, 6))   # -> 5
    print(binary_search(arr, 2))   # -> -1

    # --- Binary Search on a value range ---
    print(binary_search_range(1, 100))   # -> 10

    # --- Binary Search Tree search ---
    #         5
    #       /   \
    #      3     8
    #     / \   / \
    #    1   4 6   9
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(8)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print(search(root, 6))    # -> True
    print(search(root, 7))    # -> False