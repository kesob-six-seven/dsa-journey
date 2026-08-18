from collections import deque

# ==========================================
# 1. DOUBLY LINKED LIST
# ==========================================
class DoublyNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev  # The extra pointer going backwards

# Creating the list: 1 <-> 2
node1 = DoublyNode(1)
node2 = DoublyNode(2)

# Wiring both directions
node1.next = node2
node2.prev = node1

# ==========================================
# 2. QUEUES (First-In-First-Out)
# ==========================================
# NEVER use a standard Python list `[]` for a queue. 
# pop(0) on a standard list is an O(N) operation.
# ALWAYS use collections.deque for O(1) appends and pops.

queue = deque()

# Enqueue (Add to the back)
queue.append(1)
queue.append(2)
queue.append(3)
# queue is now: deque([1, 2, 3])

# Dequeue (Remove from the front)
first_item = queue.popleft()  # returns 1 in O(1) time