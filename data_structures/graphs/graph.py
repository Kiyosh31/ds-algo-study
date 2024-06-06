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


# Better for CODING INTERVIEWS
# Key -> Node
# Value -> list of neighbors
adjList = {"A": [], "B": []}

# Given a list of edges, build an adjacency list
# This means Node A is connected to Node B
edges = [
    ["A", "B"],
    ["B", "C"],
    ["B", "E"],
    ["C", "E"],
    ["E", "D"]
]

adj_list = {}

for source, destination in edges:
    if source not in adj_list:
        adj_list[source] = []
    if destination not in adj_list:
        adj_list[destination] = []
    adj_list[source].append(destination)

print(adj_list)
