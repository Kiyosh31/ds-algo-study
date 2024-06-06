"""
BFS

Find the length of the shortest path from the top left 
of the grid to the bottom right.

Time complexity
O(m*n)
"""

# Matrix (2D Grid)
grid = [[0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]]


def bfs():
    """bfs in graph"""
    ROWS, COLS = len(grid), len(grid[0])
    visit = set()
    queue = []
    queue.append((0, 0))
    visit.add((0, 0))

    length = 0
    while queue:
        for _ in range(len(queue)):
            r, c = queue.pop(0)
            if r == ROWS - 1 and c == COLS - 1:
                return length

            neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in neighbors:
                if (min(r + dr, c + dc) < 0 or
                    r + dr == ROWS or c + dc == COLS or
                        (r + dr, c + dc) in visit or grid[r + dr][c + dc] == 1):
                    continue
                queue.append((r + dr, c + dc))
                visit.add((r + dr, c + dc))
        length += 1


print(bfs())
