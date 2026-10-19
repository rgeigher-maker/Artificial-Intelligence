def hill_climbing(f, x0, neighbor):
    x = x0
    path = [x]
    while True:
        neighbors = neighbor(x)
        if not neighbors:
            break
        best_neighbor = max(neighbors, key=f)

        if f(best_neighbor) < f(x):
            break

        x = best_neighbor
        path.append(x)
    return path


graph = {
    'A': ['B', 'C', 'U'],
    'B': ['E', 'G'],
    'C': ['G', 'I', 'J'],
    'U': ['K', 'Y'],
    'E': ['G', 'M'],
    'G': ['M'],
    'I': ['M'],
    'J': ['K', 'M'],
    'K': ['J', 'M'],
    'Y': ['M'],
    'M': []
}

heuristics = {
    'A': 7, 'B': 5, 'C': 3, 'U': 4,
    'E': 2, 'G': 3, 'I': 6, 'J': 4,
    'K': 1, 'Y': 2, 'M': 0
}


def objective_function(node):
    return -heuristics[node]


def get_neighbors(node):
    return graph[node]


if __name__ == "__main__":
    initial_state = 'A'
    solution_path = hill_climbing(objective_function, initial_state, get_neighbors)

    total_cost = len(solution_path) - 1

    print("Path:", " -> ".join(solution_path))
    print("Total Cost:", total_cost)
