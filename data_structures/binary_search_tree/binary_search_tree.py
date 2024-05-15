"""
Binary tree

left = lesser
right = greater
"""


class TreeNode:
    """Treenode"""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"value: {self.val}, left: {self.left}, right: {self.right}"


def insert(root, val):
    """Insert a new node and return the root of the BST."""
    if not root:
        return TreeNode(val)

    if val > root.val:
        root.right = insert(root.right, val)
    elif val < root.val:
        root.left = insert(root.left, val)
    return root


def min_value_node(root):
    """Return the minimum value node of the BST."""
    curr = root
    while curr and curr.left:
        curr = curr.left
    return curr


def remove(root, val):
    """Remove a node and return the root of the BST."""
    if not root:
        return None

    if val > root.val:
        root.right = remove(root.right, val)
    elif val < root.val:
        root.left = remove(root.left, val)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            min_node = min_value_node(root.right)
            root.val = min_node.val
            root.right = remove(root.right, min_node.val)
    return root


def breadth_first_search(root):
    """it traverse the tree by level"""
    queue = []  # Queue

    if root:
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.pop(0)
            print(curr.val)
            if curr.left:
                queue.append(curr.val)
            if curr.right:
                queue.append(curr.right)
        level += i


bst = TreeNode(4)
insert(bst, 3)
insert(bst, 6)
insert(bst, 2)
insert(bst, 5)
insert(bst, 7)
# print(bst)
breadth_first_search(bst)
