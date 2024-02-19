"""Singly linked list"""


class Node:
    """Node for singly linked list"""

    def __init__(self, value) -> None:
        """constructor"""
        self.value = value
        self.next = None


class LinkedList:
    """Singly linked list"""

    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        """append a node at the end of the list"""
        aux = Node(value)
        self.tail.next = aux
        self.tail = aux

    def prepend(self, value):
        """prepend a node at the beginning of the list"""
        aux = Node(value)
        aux.next = self.head
        self.head = aux

    def insert(self, value):
        """Insert a node at any place of the list"""

        if self.head.value == value:
            self.prepend(value)
        elif self.tail.value == value:
            self.append(value)
        else:
            pass

    def delete_beginning(self):
        """deletes a node at the beginning of the list"""

    def delete_end(self):
        """deletes a node at the end of the list"""

    def delete(self, value):
        """Deletes a node at any place of the list"""

    def print(self):
        """prints the list"""
        aux = self.head
        while aux is not None:
            print(aux.value)
            aux = aux.next


my_list = LinkedList(1)
my_list.insert(2)
my_list.insert(3)
my_list.insert(4)
my_list.insert(5)
my_list.print()

# my_list.delete(3)
# my_list.print()
