"""
Binary tree

left = lesser
right = greater
"""


class Node:
    """Node"""

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    """Binary tree"""

    def __init__(self, value) -> None:
        aux = Node(value)
        self.root = aux

    def insert(self, root, value):
        """inserts a new leaf to the tree"""
        if root is None:
            aux = Node(value)
            self.root = aux
        else:
            if value > root.value:
                root.right = self.insert(root.right, value)
            elif value < root.value:
                root.left = self.insert(root.left, value)
            else:
                return root

    def min_value_node(self, root):
        """finds the minumum value node"""
        curr = root
        while curr and curr.left:
            curr = curr.left
        return curr

    def remove(self, root, val):
        """remove a node from the tree"""
        if not root:
            return None

        # Case: 0 or 1 leaf nodes
        if val > root.value:
            root.right = self.remove(root.right, val)
        elif val < root.value:
            root.left = self.remove(root.left, val)
        else:
            # Case: 2 leaf nodes
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                min_node = self.min_value_node(root.right)
                root.value = min_node.val
                root.right = self.remove(root.right, min_node.value)
        return root

    def search(self, root, target):
        """search a node in tree"""
        if root is None:
            return

        if target > self.root.value:
            return self.search(root.right, target)
        elif target < self.root.value:
            return self.search(root.left, target)
        else:
            return True


bst = BinarySearchTree(5)
bst.insert(bst.root, 3)
bst.insert(bst.root, 7)
bst.insert(bst.root, 2)
bst.insert(bst.root, 4)
bst.insert(bst.root, 6)
bst.insert(bst.root, 8)
