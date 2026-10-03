"""
Day 89 — NeetCode 150: Tries Complete
Implement Trie | Design Add and Search Words | Word Search II
"""

from typing import List


# ============================================================
# 1. IMPLEMENT TRIE PREFIX TREE (LC 208) — Medium
# ============================================================

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class Trie:
    """
    Each node stores a dict of children and an end flag.
    Insert walks/creates nodes char by char, marking end at last char.
    Search checks end flag. StartsWith just checks path exists.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.end

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True


# ============================================================
# 2. DESIGN ADD AND SEARCH WORDS (LC 211) — Medium
# ============================================================

class WordDictionary:
    """
    Same as Trie but search supports '.' wildcard — when '.' is seen,
    recurse into ALL children and return True if any path matches.
    """

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    return any(dfs(i + 1, child) for child in node.children.values())
                if c not in node.children:
                    return False
                node = node.children[c]
            return node.end

        return dfs(0, self.root)


# ============================================================
# 3. WORD SEARCH II (LC 212) — Hard
# ============================================================

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        Build a Trie from all words. DFS on board — at each cell follow
        the Trie path. When a word end is found, add to results and mark
        visited to avoid revisiting. Prune dead Trie branches for speed.
        """
        root = TrieNode()
        for word in words:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.end = True

        rows, cols = len(board), len(board[0])
        res = []

        def dfs(r, c, node, path):
            if (r < 0 or c < 0 or r >= rows or c >= cols or
                    board[r][c] not in node.children):
                return
            tmp = board[r][c]
            node = node.children[tmp]
            path += tmp
            board[r][c] = "#"

            if node.end:
                res.append(path)
                node.end = False  # avoid duplicates

            dfs(r+1, c, node, path)
            dfs(r-1, c, node, path)
            dfs(r, c+1, node, path)
            dfs(r, c-1, node, path)

            board[r][c] = tmp

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return res