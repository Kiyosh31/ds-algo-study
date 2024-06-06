"""
Dfs/Backtracking

Count the unique paths from the top left to the bottom right.
A single path may only move along 0's and can't visit same cell
more than once.
"""

# Count paths


def dfs(node, target, adj_list, visit):
    """DFS (backtracking) using hashmap"""
    if node in visit:
        return 0
    if node == target:
        return 1

    count = 0
    visit.add(node)
    for neighbor in adj_list[node]:
        count += dfs(neighbor, target, adj_list, visit)
    visit.remove(node)

    return count


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


print(dfs("A", "E", adj_list, set()))
