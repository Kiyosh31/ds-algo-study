"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []
"""

# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def reverse_list(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    prev = None
    current = head

    while current:
        nxt = current.next
        current = prev
        prev = current
        current = nxt
    return prev
