def tsp_greedy(nodes, edges, start):
    path = []
    visited = set()
    current_node = start
    total_weight = 0
    while len(path) < len(nodes):
        visited.add(current_node)
        path.append(current_node)
        next_node = None
        min_weight = float('inf')
        for node, weight in edges[current_node].items():
            if node not in visited and weight < min_weight:
                next_node = node
                min_weight = weight
        if next_node is None:
            break
        current_node = next_node
        total_weight += min_weight
    # Return to the starting node
    path.append(start)
    total_weight += edges[path[-2]][start]
    return total_weight, path


# Test case 1: 4 nodes
nodes = ['A', 'B', 'C', 'D']
edges = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'C': 4, 'D': 6},
    'C': {'A': 3, 'B': 4, 'D': 5},
    'D': {'A': 1, 'B': 6, 'C': 5}
}
start = 'A'
print(tsp_greedy(nodes, edges, start))  # Prints (12, ['A', 'D', 'C', 'B', 'A'])


# Test case 2: 5 nodes
nodes = ['A', 'B', 'C', 'D', 'E']
edges = {
    'A': {'B': 2, 'C': 4, 'D': 1, 'E': 3},
    'B': {'A': 2, 'C': 1, 'D': 3, 'E': 4},
    'C': {'A': 4, 'B': 1, 'D': 2, 'E': 5},
    'D': {'A': 1, 'B': 3, 'C': 2, 'E': 6},
    'E': {'A': 3, 'B': 4, 'C': 5, 'D': 6}
}
start = 'A'
print(tsp_greedy(nodes, edges, start))  # Prints (11, ['A', 'D', 'C', 'B', 'E', 'A'])


# Test case 3: 6 nodes
nodes = ['A', 'B', 'C', 'D', 'E', 'F']
edges = {
    'A': {'B': 3, 'C': 1, 'D': 2, 'E': 5, 'F': 4},
    'B': {'A': 3, 'C': 4, 'D': 6, 'E': 2, 'F': 3},
    'C': {'A': 1, 'B': 4, 'D': 3, 'E': 4, 'F': 2},
    'D': {'A': 2, 'B': 6, 'C': 3, 'E': 1, 'F': 5},
    'E': {'A': 5, 'B': 2, 'C': 4, 'D': 1, 'F': 6},
    'F': {'A': 4, 'B': 3, 'C': 2, 'D': 5, 'E': 6}
}
start = 'A'
print(tsp_greedy(nodes, edges, start))  # Prints (11, ['A', 'C', 'F', 'B', 'E', 'D', 'A'])


# Test case 4: 7 nodes
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
edges = {
    'A': {'B': 4, 'C': 1, 'D': 3, 'E': 7, 'F': 5, 'G': 6},
    'B': {'A': 4, 'C': 6, 'D': 5, 'E': 3, 'F': 2, 'G': 7},
    'C': {'A': 1, 'B': 6, 'D': 4, 'E': 2, 'F': 7, 'G': 3},
    'D': {'A': 3, 'B': 5, 'C': 4, 'E': 6, 'F': 1, 'G': 2},
    'E': {'A': 7, 'B': 3, 'C': 2, 'D': 6, 'F': 4, 'G': 5},
    'F': {'A': 5, 'B': 2, 'C': 7, 'D': 1, 'E': 4, 'G': 6},
    'G': {'A': 6, 'B': 7, 'C': 3, 'D': 2, 'E': 5, 'F': 6}
}
start = 'A'
print(tsp_greedy(nodes, edges, start))  # Prints (17, ['A', 'C', 'E', 'B', 'F', 'D', 'G', 'A'])


# Test case 5: 8 nodes
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
edges = {
    'A': {'B': 5, 'C': 2, 'D': 4, 'E': 8, 'F': 7, 'G': 3, 'H': 1},
    'B': {'A': 5, 'C': 3, 'D': 7, 'E': 5, 'F': 6, 'G': 4, 'H': 2},
    'C': {'A': 2, 'B': 3, 'D': 6, 'E': 4, 'F': 5, 'G': 7, 'H': 8},
    'D': {'A': 4, 'B': 7, 'C': 6, 'E': 3, 'F': 2, 'G': 1, 'H': 5},
    'E': {'A': 8, 'B': 5, 'C': 4, 'D': 3, 'F': 1, 'G': 6, 'H': 7},
    'F': {'A': 7, 'B': 6, 'C': 5, 'D': 2, 'E': 1, 'G': 8, 'H': 3},
    'G': {'A': 3, 'B': 4, 'C': 7, 'D': 1, 'E': 6, 'F': 8, 'H': 4},
    'H': {'A': 1, 'B': 2, 'C': 8, 'D': 5, 'E': 7, 'F': 3, 'G': 4}
}
start = 'A'
print(tsp_greedy(nodes, edges, start))  # Prints (17, ['A', 'H', 'B', 'C', 'E', 'F', 'D', 'G', 'A'])