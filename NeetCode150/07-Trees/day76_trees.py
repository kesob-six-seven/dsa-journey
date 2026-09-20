"""
Day 76 — NeetCode 150: Trees
Count Good Nodes | Validate BST | Kth Smallest Element in BST
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# 1. COUNT GOOD NODES IN BINARY TREE (LC 1448) — Medium
# ============================================================

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        A node is "good" if no value along the path from root to it
        is greater than it. Pass the running max down the DFS — if
        current node's value >= max, it's a good node.
        """
        def dfs(node, maxVal):
            if not node:
                return 0
            good = 1 if node.val >= maxVal else 0
            maxVal = max(maxVal, node.val)
            return good + dfs(node.left, maxVal) + dfs(node.right, maxVal)

        return dfs(root, root.val)


# ============================================================
# 2. VALIDATE BINARY SEARCH TREE (LC 98) — Medium
# ============================================================

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Pass valid (min, max) bounds down the tree. Every node must
        strictly fall within its inherited bounds — not just be greater
        than its left child or less than its right child locally.
        """
        def dfs(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            return (dfs(node.left, min_val, node.val) and
                    dfs(node.right, node.val, max_val))

        return dfs(root, float("-inf"), float("inf"))


# ============================================================
# 3. KTH SMALLEST ELEMENT IN BST (LC 230) — Medium
# ============================================================

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Inorder traversal of a BST gives nodes in sorted ascending order.
        Count nodes visited — the k-th one is the answer.
        """
        self.k = k
        self.res = None

        def inorder(node):
            if not node or self.res is not None:
                return
            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.res