"""
Graph

1. Matrix
2. Adyacency Matrix
3. Adyacency List
"""

# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]

# Adjacency matrix
adjMatrix = [[0, 0, 0, 0],
             [1, 1, 0, 0],
             [0, 0, 0, 1],
             [0, 1, 0, 0]]

# GraphNode used for adjacency list


class GraphNode:
    """Graphnode"""

    def __init__(self, val):
        self.val = val
        self.neighbors = []
