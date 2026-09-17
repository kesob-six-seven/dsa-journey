"""
Day 73 — NeetCode 150: Linked List Complete
Merge K Sorted Lists | Reverse Nodes in K Group
"""

from typing import Optional, List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ============================================================
# 1. MERGE K SORTED LISTS (LC 23) — Hard
# ============================================================

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Min heap stores (val, index, node) — index breaks ties since
        ListNode isn't comparable. Always extract the smallest node
        across all lists and push its next node into the heap.
        """
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode()
        curr = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# ============================================================
# 2. REVERSE NODES IN K GROUP (LC 25) — Hard
# ============================================================

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        Check if k nodes exist ahead before reversing. Reverse the group
        in place, then recursively handle the rest and connect back.
        If fewer than k nodes remain, leave them as is.
        """
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1

        if count < k:
            return head

        prev, curr = None, head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        head.next = self.reverseKGroup(curr, k)
        return prev