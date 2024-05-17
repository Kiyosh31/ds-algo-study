"""
Binary Search Tree

left = lesses
right = greater
"""


class TreeNode:
    """Tree Node"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def search(root, target):
    """Search for a node in tree"""
    if not root:
        return False

    if target > root.value:
        return search(root.right, target)
    elif target < root.value:
        return search(root.left, target)

    return True


def insert(root, value):
    """Insert a node in tree"""
    if not root:
        return TreeNode(value)

    if value > root.value:
        root.right = insert(root.right, value)
    elif value < root.value:
        root.left = insert(root.left, value)
    return root


def min_value(root):
    """Return the minimum value of tree"""
    curr = root

    while curr and curr.left:
        curr = curr.left

    return curr


def remove(root, value):
    """Remove a node and return the root of the tree"""
    if not root:
        return

    if value > root.value:
        root.right = remove(root.right, value)
    elif value < root.value:
        root.left = remove(root.left, value)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            min_node = min_value(root.right)
            root.value = min_node.value
            root.right = remove(root.right, min_node.value)
    return root


def inorder(root):
    """Traverse"""
    if not root:
        return

    inorder(root.left)
    print(root.value)
    inorder(root.right)


def preorder(root):
    """Traverse"""
    if not root:
        return

    print(root.value)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    """Traverse"""
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.value)


def bfs(root):
    """Breadth First Search"""
    queue = []

    if root:
        queue.append(root)

    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for _ in range(len(queue)):
            curr = queue.pop(0)
            print(curr.value)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1


bst = TreeNode(4)
bst = insert(bst, 3)
bst = insert(bst, 6)
bst = insert(bst, 2)
bst = insert(bst, 5)
bst = insert(bst, 7)

print("Traverse inorder")
inorder(bst)

print("Traverse preorder")
preorder(bst)

print("Traverse postoder")
postorder(bst)

print("Breadth First Search")
bfs(bst)

print("Does 3 exist in tree? ", search(bst, 3))
print("Does 15 exist in tree? ", search(bst, 15))

bst = remove(bst, 6)
