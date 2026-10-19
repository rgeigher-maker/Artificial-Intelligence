graph = {
    "S": [("A", 3), ("B", 2), ("C", 5)],
    "A": [("G", 2), ("C", 3)],
    "B": [("A", 4), ("D", 6)],
    "C": [("B", 4), ("H", 3)],
    "H": [("A", 4), ("D", 4)],
    "G": [("E", 5), ("D", 4)],
    "D": [("E", 2), ("F", 3)],
    "E": [("F", 5)],
    "F": [],
}
heuristics = {
    "S": 10,
    "A": 8,
    "B": 9,
    "C": 7,
    "D": 4,
    "E": 3,
    "F": 0,
    "G": 6,
    "H": 6,
}


def aStarSearch(start, goal):
    open = {start}
    g = {start: 0}
    parent = {}

    while open:
        current = min(open, key=lambda n: g[n] + heuristics[n])

        if current == goal:
            path = [goal]
            while current in parent:
                current = parent[current]
                path.append(current)
            return path[::-1], g[goal]

        open.remove(current)

        for neighbor, weight in graph.get(current, []):
            tentative_g = g[current] + weight

            if tentative_g < g.get(neighbor, float("inf")):
                g[neighbor] = tentative_g
                parent[neighbor] = current
                open.add(neighbor)

    return None, float("inf")

path, total = aStarSearch("S", "F")

print("Path:", " -> ".join(path))
print("Total Cost:", total)



















