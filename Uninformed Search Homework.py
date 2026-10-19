from collections import deque

def bfs(start,end):
    queue = deque([(start, [start])])
    visited = []

    while queue:
        current, path = queue.popleft()
        visited.append(current)

        if current == end:
            return visited, path

        leftChild = 2 * current
        rightChild = 2 * current + 1

        queue.append((leftChild, path + [leftChild]))
        queue.append((rightChild, path + [rightChild]))

    return visited, []

start = 1
goal = 11
visited, path = bfs(start, goal)

print(f"Visited: {visited}")
print(f"Path to goal {goal}: {' -> '.join(map(str, path))}")


















