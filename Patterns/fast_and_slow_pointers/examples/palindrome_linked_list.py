"""
Given the head of a linked list, your task is to check whether
the linked list is a palindrome or not. Return TRUE if the linked list
is a palindrome; otherwise, return FALSE.
"""


# class LinkedListNode:
#     """__init__ will be used to make a LinkedListNode type object."""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next


def is_palindrome(head):
    """Return true/false if linkedlist is palindrome"""
    fast = head
    slow = head

    # find middle
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # reverse second half
    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    # check palindrome
    left, right = head, prev
    while right is not None:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
