"""
Day 75 — NeetCode 150: Trees
Lowest Common Ancestor of BST | Binary Tree Level Order Traversal | 
Binary Tree Right Side View
"""

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# 1. LOWEST COMMON ANCESTOR OF BST (LC 235) — Medium
# ============================================================

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        BST property tells us exactly which way to go. If both p and q
        are smaller than root, LCA must be in left subtree. If both
        larger, right subtree. Otherwise root IS the LCA.
        """
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root


# ============================================================
# 2. BINARY TREE LEVEL ORDER TRAVERSAL (LC 102) — Medium
# ============================================================

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)

        return res


# ============================================================
# 3. BINARY TREE RIGHT SIDE VIEW (LC 199) — Medium
# ============================================================

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS level order — last node in each level is visible from
        the right side. Just take the rightmost node per level.
        """
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if i == len(queue):
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(node.val)

        return res