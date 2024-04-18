"""
Given the head of a singly linked list, return the middle node of the 
linked list. If the number of nodes in the linked list is even, 
there will be two middle nodes, so return the second one.
"""


# class Node:
#     """__init__ will be used to make a LinkedListNode type object."""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next


def get_middle_node(head):
    """Return the middle node of linked list"""
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast is None or fast.next is None:
            return slow
    return slow
