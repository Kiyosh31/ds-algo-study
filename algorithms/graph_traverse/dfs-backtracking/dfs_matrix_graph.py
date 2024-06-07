"""
Dfs/Backtracking

Count the unique paths from the top left to the bottom right.
A single path may only move along 0's and can't visit same cell
more than once.


Time complexity
4 ^nm

Space complexity
O(m*n)
"""

# Grid -> the matrix
# r -> coordX
# c -> coordY
# visit -> flag to know if this node is visitted


def dfs(matrix_graph, r, c, visit):
    """traverse a graph to find the exit path"""
    # take out the dimensions of the matrix
    rows, cols = len(matrix_graph), len(matrix_graph[0])

    # check if the actual position is out of matrix
    # did we visitted this position or
    # is this position blocked
    if min(r, c) < 0 or r == rows or c == cols or (r, c) in visit or matrix_graph[r][c] == 1:
        return 0

    # did we reached the destination?
    if r == rows - 1 and c == cols - 1:
        return 1

    # mark this coord as visitted
    visit.add((r, c))

    # This count is to know how many resolution paths exist on the matrix
    count = 0
    # we move in all directions (up, down, left, right)
    count += dfs(matrix_graph, r + 1, c, visit)
    count += dfs(matrix_graph, r - 1, c, visit)
    count += dfs(matrix_graph, r, c + 1, visit)
    count += dfs(matrix_graph, r, c - 1, visit)

    # mark this coord as unvisitted
    visit.remove((r, c))
    return count


matrix = [
    [0, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 0, 0, 1],
    [0, 1, 0, 0]
]
print(dfs(matrix, 0, 0, set()))
