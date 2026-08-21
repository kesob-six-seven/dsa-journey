"""
Day 47 — Binary Search Trees: Insert & Delete, DFS, BFS

Covers:
1. BST Insert (LC 701)
2. BST Delete (LC 450)
3. DFS Traversals — Inorder (LC 94), Preorder, Postorder
4. BFS / Level Order Traversal (LC 102)
5. BST as a Set/Map — conceptual note (BSTs give O(log n) sorted 
   insert/search/delete, unlike hash-based sets/maps which are O(1) 
   average but unordered)
"""

import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# -------------------------------------------------
# 1. Insert into a Binary Search Tree — LC 701
# -------------------------------------------------
class InsertBST:
    def insertIntoBST(self, root, val):
        """
        THEORY:
        BST property: left < root < right.
        Recurse in the direction the value belongs, and insert
        a new node when we hit an empty spot (None).

        TC: O(H) where H = tree height (O(log N) balanced, O(N) worst case)
        SC: O(H) recursion stack
        """
        if not root:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root


# -------------------------------------------------
# 2. Delete Node in a BST — LC 450
# -------------------------------------------------
class DeleteBST:
    def deleteNode(self, root, key):
        """
        THEORY:
        Three cases once the target node is found:
        1. No left child -> replace node with its right subtree
        2. No right child -> replace node with its left subtree
        3. Two children -> find the inorder successor (smallest value
           in the right subtree = leftmost node), copy its value into
           the current node, then delete that successor from the
           right subtree (recursively — it has at most one child).

        TC: O(H) where H = tree height
        SC: O(H) recursion stack
        """
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # find inorder successor (leftmost node in right subtree)
            cur = root.right
            while cur.left:
                cur = cur.left
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)

        return root


# -------------------------------------------------
# 3. DFS Traversals
# -------------------------------------------------
class DFSTraversals:
    def inorder(self, root):
        """LC 94 — Inorder: Left -> Root -> Right (sorted order for a BST)."""
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res

    def preorder(self, root):
        """Preorder: Root -> Left -> Right."""
        res = []

        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return res

    def postorder(self, root):
        """Postorder: Left -> Right -> Root."""
        res = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res


# -------------------------------------------------
# 4. Binary Tree Level Order Traversal (BFS) — LC 102
# -------------------------------------------------
class BFSTraversal:
    def levelOrder(self, root):
        """
        THEORY:
        Standard BFS using a queue. Process one full level at a time
        by snapshotting the current queue length before looping.

        TC: O(N) — every node visited once
        SC: O(N) — queue can hold up to a full level of nodes
        """
        res = []
        if not root:
            return res

        q = collections.deque([root])

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)

        return res


# -------------------------------------------------
# 5. BST as Sets and Maps — conceptual note
# -------------------------------------------------
# A BST can implement a Set (unique keys) or Map (key-value pairs)
# by storing keys in sorted order via the BST property.
#
# vs. Hash Set/Map:
#   - Hash-based: O(1) average insert/search/delete, but unordered.
#   - BST-based:  O(log N) insert/search/delete (if balanced), 
#                 but maintains sorted order — enables range queries,
#                 min/max lookup, and in-order iteration for free.
#
# Python's dict/set are hash-based. Languages like C++ (map/set) and
# Java (TreeMap/TreeSet) offer BST-backed (typically Red-Black Tree)
# ordered alternatives.