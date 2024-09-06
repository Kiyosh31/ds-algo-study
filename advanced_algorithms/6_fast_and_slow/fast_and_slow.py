"""
Fast and Slow pointers

Q: Find the middle of a linkedlist
Input: 1 -> 2 -> 3 -> 4 -> 5 -> None
Output: 3
"""
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
from data_structures.list_node.list_node import ListNode, insert_node, print_list_arr, create_cycle


def middle_of_list(head):
    """
    Time: O(n)
    Space: O(1)
    """
    fast, slow = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val


list1 = ListNode(1)
insert_node(list1, 2)
insert_node(list1, 3)
insert_node(list1, 4)
insert_node(list1, 5)
print_list_arr(list1)

print("Middle: ", middle_of_list(list1))


# Q: Determine if a linked list contains a cycle.


def has_cycle(head):
    """
    Time complexity: O(n)
    Space complexity: O(1)
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

print()
list2 = ListNode(1)
insert_node(list2, 2)
insert_node(list2, 3)
insert_node(list2, 4)
insert_node(list2, 5)
# create_cycle(list2, 2)
print_list_arr(list2)


# Q: Determine if a linked list has a cycle and return the head


def cycle_start(head):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if not fast or not fast.nex:
        return None

    slow2 = head
    while slow != slow2:
        slow = slow.next
        slow2 = slow2.next
    return slow
