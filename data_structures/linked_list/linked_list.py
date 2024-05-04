"""Singly Linked List"""


class Node:
    """list node"""

    def __init__(self, value) -> None:
        self.next = None
        self.value = value


class LinkedList:
    """Linked list"""

    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        """add a new node at the end of the list"""
        aux = Node(value)

        if self.head is None:
            self.head = aux
            self.tail = aux
        else:
            self.tail.next = aux
            self.tail = aux

    def prepend(self, value):
        """add a new node at the beginning of the list"""
        aux = Node(value)

        if self.head is None:
            self.head = aux
            self.tail = aux
        else:
            aux.next = self.head
            self.head = aux

    def print(self):
        """prints the list"""
        curr = self.head
        while curr:
            print(curr.value)
            curr = curr.next

    def pop_end(self):
        """deletes a node at the end"""
        if self.head is None:
            return

        curr = self.head
        while curr.next.next is not None:
            curr = curr.next

        curr.next = None
        self.tail = curr

    def pop_first(self):
        """deletes a node at the begining"""
        if self.head is None:
            return

        self.head = self.head.next


print("List:")
my_list = LinkedList(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.prepend(6)
my_list.print()
print()

print("Pop first")
my_list.pop_first()
my_list.print()
print()

print("Pop end")
my_list.pop_end()
my_list.print()
