"""
Day 74 — NeetCode 150: Trees
Invert Binary Tree | Maximum Depth | Diameter | 
Balanced Binary Tree | Same Tree | Subtree of Another Tree
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# 1. INVERT BINARY TREE (LC 226) — Easy
# ============================================================

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


# ============================================================
# 2. MAXIMUM DEPTH OF BINARY TREE (LC 104) — Easy
# ============================================================

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


# ============================================================
# 3. DIAMETER OF BINARY TREE (LC 543) — Easy
# ============================================================

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Diameter at any node = left height + right height. Track the
        max across all nodes via a nonlocal variable during DFS.
        """
        self.res = 0

        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            self.res = max(self.res, left + right)
            return 1 + max(left, right)

        dfs(root)
        return self.res


# ============================================================
# 4. BALANCED BINARY TREE (LC 110) — Easy
# ============================================================

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        DFS returns [isBalanced, height] tuple bottom-up. Both conditions
        checked together — no separate height computation needed.
        """
        def dfs(root):
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right)
            balanced = (left[0] and right[0]) and abs(left[1] - right[1]) <= 1
            return [balanced, 1 + max(left[1], right[1])]

        return dfs(root)[0]


# ============================================================
# 5. SAME TREE (LC 100) — Easy
# ============================================================

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# ============================================================
# 6. SUBTREE OF ANOTHER TREE (LC 572) — Easy
# ============================================================

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)