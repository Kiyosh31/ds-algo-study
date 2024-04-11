"""
Check whether or not a linked list contains a cycle. 
If a cycle exists, return TRUE. Otherwise, return FALSE. 
The cycle means that at least one node can be reached again by 
traversing the next pointer.
"""


class LinkedListNode:
    """__init__ will be used to make a LinkedListNode type object."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def detect_cycle(head):
    """Return true/false if list is cycled"""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
