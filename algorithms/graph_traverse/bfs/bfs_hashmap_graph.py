"""
BFS

Find the length of the shortest path from the top left
of the grid to the bottom right.

"""


# Shortest path from node to target
def bfs(node, target, adj_list):
    """"""
    length = 0
    visit = set()
    visit.add(node)
    queue = []
    queue.append(node)

    while queue:
        for _ in range(len(queue)):
            curr = queue.pop(0)
            if curr == target:
                return length

            for neighbor in adj_list[curr]:
                if neighbor not in visit:
                    visit.add(neighbor)
                    queue.append(neighbor)
        length += 1
    return length


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

print(bfs("A", "E", adj_list))