"""
ListNode

This is the usual DS for coding challenge problems
"""


class ListNode:
    """ListNode"""

    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next


def insert_node(head, val):
    """Inserts a new node in list"""
    new_node = ListNode(val)

    curr = head
    while curr.next:
        curr = curr.next

    curr.next = new_node

def create_cycle(head, target_val):
    """create cycle in list"""
    # Find the node with the target value
    curr = head
    while curr and curr.val != target_val:
        curr = curr.next

    # If the target value is not found, return without cycling
    if not curr:
        return

    # Find the last node
    last_node = head
    while last_node.next:
        last_node = last_node.next

    # Connect the last node to the target node
    last_node.next = curr

def print_list_arr(head):
    """prints the whole list in arr shape"""
    list_arr = []

    curr = head
    while curr:
        list_arr.append(curr.val)
        curr = curr.next
    print(list_arr)

def print_list(head):
    """prints the whole list"""
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next


# linked_list = ListNode(1)
# insert_node(linked_list, 2)
# insert_node(linked_list, 3)
# insert_node(linked_list, 4)
# insert_node(linked_list, 5)
# print_list(linked_list)
