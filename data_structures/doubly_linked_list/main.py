"""Doubly Linked List"""


class Node:
    """List node"""

    def __init__(self, value) -> None:
        self.next = None
        self.prev = None
        self.value = value


class DoublyLinkedList:
    """Doubly Linked List"""

    def __init__(self, value) -> None:
        """Constructor"""
        aux = Node(value)
        self.head = aux
        self.tail = aux

    def append(self, value):
        """adds a new node at the beginning of the list"""
        aux = Node(value)

        if self.head is None:
            self.head = aux
            self.tail = aux
        else:
            self.tail.next = aux
            self.tail = aux

    def prepend(self, value):
        """adds a new node at the end of the list"""
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
        """deletes a node at the end of the list"""
        if self.head is None:
            return

        curr = self.head
        while curr.next.next is not None:
            curr = curr.next

        self.tail = curr
        curr.next = None

    def pop_first(self):
        """deletes a node at the beginning of the list"""
        if self.head is None:
            return

        self.head = self.head.next


print("Doubly linked list")
my_list = DoublyLinkedList(0)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.print()

print("\nprepend")
my_list.prepend(7)
my_list.print()

print("\nPop end")
my_list.pop_end()
my_list.print()

print("\nPop first")
my_list.pop_first()
my_list.print()
