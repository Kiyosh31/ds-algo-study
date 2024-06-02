"""Depth first search"""


def inorder(root):
    """
    left
    value
    right
    """
    if not root:
        return

    inorder(root.left)
    print(root.value)
    inorder(root.right)


def preorder(root):
    """
    value 
    left
    right
    """
    if not root:
        return

    print(root.value)
    preorder(root.left)
    preorder(root.right)


def postorder(root):
    """
    left
    right
    value
    """
    if not root:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.value)
