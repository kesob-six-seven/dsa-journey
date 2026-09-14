"""
Day 71 — NeetCode 150: Linked List
Add Two Numbers | Find The Duplicate Number | LRU Cache
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================================
# 1. ADD TWO NUMBERS (LC 2) — Medium
# ============================================================

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Simulate addition digit by digit with a carry. Dummy node
        avoids edge cases around the head of the result list.
        """
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10

            curr.next = ListNode(val)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


# ============================================================
# 2. FIND THE DUPLICATE NUMBER (LC 287) — Medium
# ============================================================

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Floyd's cycle detection — treat array values as next pointers.
        A duplicate creates a cycle. Find the cycle entry point which
        is the duplicate number. O(1) space, no array modification.
        """
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow


# ============================================================
# 3. LRU CACHE (LC 146) — Medium
# ============================================================

class LRUCache:
    """
    Doubly linked list + hash map. List maintains order (MRU at head,
    LRU at tail). Hash map gives O(1) access to any node. On get/put,
    move the node to the head. On capacity overflow, evict from tail.
    """

    class Node:
        def __init__(self, key=0, val=0):
            self.key = key
            self.val = val
            self.prev = self.next = None

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = self.Node()  # dummy head (MRU side)
        self.tail = self.Node()  # dummy tail (LRU side)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _insert(self, node):  # insert at head (MRU)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node = self.Node(key, value)
        self.cache[key] = node
        self._insert(node)

        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]