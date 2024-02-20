"""Queue"""


class Node:
    """Node"""

    def __init__(self, value) -> None:
        """constructor"""
        self.value = value
        self.next = None


class Queue:
    """Queue"""

    def __init__(self, value) -> None:
        """constructor"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def enqueue(self, value):
        """adds a new node at the head"""
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        """deletes the last node"""
        if self.head is None:
            return

        aux = self.head
        while aux.next.next is not None:
            aux = aux.next

        value_to_return = aux.next
        self.tail = aux
        aux.next = None
        return value_to_return.value

    def front(self):
        """gets the front of the queue"""
        return self.tail.value

    def print(self):
        """prints the queue"""
        aux = self.head

        while aux is not None:
            print(aux.value)
            aux = aux.next


queue = Queue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.print()

print()
print(queue.front())

print()
print(queue.dequeue())

print()
queue.print()

print()
print(queue.dequeue())

print()
queue.print()
