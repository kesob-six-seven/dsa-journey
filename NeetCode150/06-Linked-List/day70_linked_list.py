"""
Day 70 — NeetCode 150: Linked List
Reorder List | Remove Nth Node From End of List | Copy List With Random Pointer
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================================
# 1. REORDER LIST (LC 143) — Medium
# ============================================================

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        3 steps:
        1. Find middle using slow/fast pointers.
        2. Reverse the second half.
        3. Merge the two halves alternately.
        """
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        second = slow.next
        slow.next = None
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        # Merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2


# ============================================================
# 2. REMOVE NTH NODE FROM END OF LIST (LC 19) — Medium
# ============================================================

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Two pointers gap of n — when fast hits the end, slow is exactly
        at the node before the one to remove.
        """
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy

        for _ in range(n + 1):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next


# ============================================================
# 3. COPY LIST WITH RANDOM POINTER (LC 138) — Medium
# ============================================================

class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        """
        Two passes with a hash map old -> new node.
        First pass: create all new nodes.
        Second pass: assign next and random pointers using the map.
        """
        oldToNew = {None: None}

        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr:
            oldToNew[curr].next = oldToNew[curr.next]
            oldToNew[curr].random = oldToNew[curr.random]
            curr = curr.next

        return oldToNew[head]