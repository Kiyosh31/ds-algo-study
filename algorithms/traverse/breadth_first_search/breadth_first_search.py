"""Breadth first search"""


def breadth_first_search(root):
    """it traverse the tree by level"""
    queue = []  # Queue

    if root:
        queue.append(root.value)

    level = 0
    while len(queue) > 0:
        print("level: ", level)
        for i in range(len(queue)):
            curr = queue.pop(0)
            print(curr.value)
            if curr.left:
                queue.append(curr.value)
            if curr.right:
                queue.append(curr.right)
        level += i
