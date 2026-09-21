"""
Day 77 — NeetCode 150: Trees Complete
Construct Binary Tree from Preorder and Inorder Traversal |
Binary Tree Maximum Path Sum | Serialize and Deserialize Binary Tree
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# 1. CONSTRUCT BINARY TREE FROM PREORDER AND INORDER (LC 105) — Medium
# ============================================================

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Preorder's first element is always the root. Find that root in
        inorder — everything left of it is the left subtree, everything
        right is the right subtree. Recurse with array slicing.
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root


# ============================================================
# 2. BINARY TREE MAXIMUM PATH SUM (LC 124) — Hard
# ============================================================

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        At each node, max path through it = node.val + left gain + right gain.
        But when returning to parent, can only use one side (a path can't
        branch twice). Track global max separately via nonlocal.
        """
        self.res = root.val

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.res = max(self.res, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.res


# ============================================================
# 3. SERIALIZE AND DESERIALIZE BINARY TREE (LC 297) — Hard
# ============================================================

class Codec:
    """
    dfs - it was kinda easy , easier than the last medium 
    """

    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0

        def dfs():
            if vals[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node

        return dfs()