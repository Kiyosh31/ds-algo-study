"""Breadth first search"""


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
