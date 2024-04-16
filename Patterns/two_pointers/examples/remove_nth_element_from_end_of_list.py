"""
Given a singly linked list, remove the nth
node from the end of the list and return its head.
"""


class Node:
    """__init__ will be used to make a LinkedListNode type object."""

    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def remove_nth_last_node(head, n):
    """returns head of updated linkedlist"""
    left = head
    right = head

    for _ in range(n):
        right = right.next

    if not right:
        return head.next

    while right.next:
        right = right.next
        left = left.next

    left.next = left.next.next
    return head
