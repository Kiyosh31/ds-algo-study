"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the next pointer. Internally,
pos is used to denote the index of the node that tail's next pointer 
is connected to. Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list,
where the tail connects to the 1st node (0-indexed).

Example 2
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list,
where the tail connects to the 0th node.

Example 3
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""


# This problem can be solved with 2 patterns
# 1. Two pointers
# 2. Hash Table

# Hash table solution
def detect_cycle_ht(head):
    """Return Bool if the list is cycled"""
    start = head
    seen = set()

    while start:
        if start in seen:
            return True
        else:
            seen.add(start)
            start = start.next
    return False


# Two Pointers solution
def detect_cycle_tp(head):
    """Return Bool if the list is cycled"""
    left = head
    right = head

    while right is not None and right.next is not None:
        left = left.next
        right = right.next.next

        if right == left:
            return True

    return False


class ListNode:
    """ListNode"""

    def __init__(self, x):
        self.val = x
        self.next = None


def create_linked_list(nums):
    """create list"""
    if not nums:
        return None

    head = ListNode(nums[0])
    current = head

    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next

    return head
