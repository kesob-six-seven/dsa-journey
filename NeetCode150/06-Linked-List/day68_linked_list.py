"""
Day 68 — NeetCode 150: Linked List
Reverse Linked List | Merge Two Sorted Lists | Linked List Cycle
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================================
# 1. REVERSE LINKED LIST (LC 206) — Easy
# ============================================================

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


# ============================================================
# 2. MERGE TWO SORTED LISTS (LC 21) — Easy
# ============================================================

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Dummy node trick — avoids edge cases around the head.
        Always attach the smaller node to the result chain, advance
        that list's pointer. Attach remaining nodes at the end.
        """
        dummy = ListNode()
        curr = dummy

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        curr.next = list1 if list1 else list2
        return dummy.next


# ============================================================
# 3. LINKED LIST CYCLE (LC 141) — Easy
# ============================================================

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Floyd's slow/fast pointer — slow moves 1 step, fast moves 2.
        If a cycle exists they'll eventually meet inside it.
        """
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False