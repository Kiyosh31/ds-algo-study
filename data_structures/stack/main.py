"""Stack"""


class Node:
    """Stack Node"""

    def __init__(self, value) -> None:
        """Constructor"""
        self.value = value
        self.prev = None


class Stack:
    """Stack"""

    def __init__(self, value) -> None:
        """constructor"""
        new_node = Node(value)
        self.stack_top = new_node

    def push(self, value):
        """adds a new element at the top of the stack"""
        new_node = Node(value)

        if self.stack_top is None:
            self.stack_top = new_node
        else:
            new_node.prev = self.stack_top
            self.stack_top = new_node

    def pop(self):
        """deletes the top of the stack"""
        if self.stack_top is None:
            return

        aux = self.stack_top
        self.stack_top = aux.prev

        return aux.value

    def top(self):
        """returns the top of the stack without deleting the element"""
        return self.stack_top.value

    def print(self):
        """prints the stack"""
        aux = self.stack_top

        while aux is not None:
            print(aux.value)
            aux = aux.prev


stack = Stack(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.print()

print()
print(stack.top())

print()
print(stack.pop())

print()
stack.print()
