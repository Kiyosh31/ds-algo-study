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
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, value):
        """prepend a node at the beginning of the list"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert(self, value):
        """Insert a node at any place of the list"""

        if self.head is None:
            self.prepend(value)
        elif self.tail is None:
            self.append(value)
        else:
            pass

    def pop_first(self):
        """deletes a node at the beginning of the list"""
        if self.head is None:
            return

        aux = self.head
        self.head = self.head.next
        aux.next = None

        if self.head is None:
            self.tail = None

    def pop(self):
        """deletes a node at the end of the list"""
        if self.head is None:
            return

        aux = self.head
        while aux.next is not None:
            aux = aux.next
        aux.next = None
        self.tail = aux

    def delete(self, value):
        """Deletes a node at any place of the list"""

    def print(self):
        """prints the list"""
        aux = self.head
        while aux is not None:
            print(aux.value)
            aux = aux.next

    def get(self, value):
        """Gets the index of a the node containing value"""
        aux = self.head
        index = 0

        while aux is not None:
            if aux == value:
                return index
            index = index + 1
            aux = aux.next
        return -1

    def set(self, value):
        """modifies a value of an existing node"""
        aux = self.head

        while aux is not None:
            if aux.value == value:
                aux.value = value
                break
            aux = aux.next


my_list = LinkedList(1)
my_list.insert(2)
my_list.insert(3)
my_list.insert(4)
my_list.insert(5)
my_list.print()
