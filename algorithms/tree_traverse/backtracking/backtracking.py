"""
Backtracking

Determine if a path exists from the root of the tree to a leaf node.
it may not contain any zeroes
"""


class TreeNode:
    """TreeNode"""

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    """Insert a node in tree"""
    if not root:
        return TreeNode(value)

    if value > root.value:
        root.right = insert(root.right, value)
    elif value < root.value:
        root.left = insert(root.left, value)
    return root


def backtracking(root):
    """Returns True/False if path exists from root to leaf"""
    if not root or root.value == 0:
        return False

    if not root.left and not root.right:
        return True
    if backtracking(root.left):
        return True
    if backtracking(root.right):
        return True
    return False


def backtracking_path(root, tree_path):
    """returns the path"""
    if not root or root.value == 0:
        return False
    tree_path.append(root.value)

    if not root.left and not root.right:
        return True
    if backtracking_path(root.left, tree_path):
        return True
    if backtracking_path(root.right, tree_path):
        return True
    tree_path.pop()
    return False


bst = TreeNode(4)
bst = insert(bst, 0)
bst = insert(bst, 1)
bst = insert(bst, 7)
bst = insert(bst, 2)
bst = insert(bst, 0)

print(backtracking(bst))

# Initialize the path list
path = []
backtracking_path(bst, path)
print(path)
