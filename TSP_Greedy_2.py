def tsp_greedy(G, start):
    visited = []
    current = start
    total_weight = 0
    path = []

    # Visit all nodes in the graph
    while len(visited) < len(G):
        visited.append(current)
        min_weight = float('inf')
        next_node = None

        # Find the closest unvisited node
        for node, weight in G[current].items():
            if node not in visited and weight < min_weight:
                min_weight = weight
                next_node = node

        # Add the edge to the path and update the total weight if a next node was found
        if next_node is not None:
            path.append((current, next_node, min_weight))
            total_weight += min_weight
            current = next_node

    # Return to the start node
    path.append((current, start, G[current][start]))
    total_weight += G[current][start]

    return (total_weight, path)


# Test case 1: 4 nodes
G = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'C': 4, 'D': 6},
    'C': {'A': 3, 'B': 4, 'D': 5},
    'D': {'A': 1, 'B': 6, 'C': 5}
}
print(tsp_greedy(G, 'A'))  # Prints (12, [('A', 'D', 1), ('D', 'C', 5), ('C', 'B', 4), ('B', 'A', 2)])


# Test case 2: 5 nodes
G = {
    'A': {'B': 2, 'C': 4, 'D': 1, 'E': 3},
    'B': {'A': 2, 'C': 1, 'D': 3, 'E': 4},
    'C': {'A': 4, 'B': 1, 'D': 2, 'E': 5},
    'D': {'A': 1, 'B': 3, 'C': 2, 'E': 6},
    'E': {'A': 3, 'B': 4, 'C': 5, 'D': 6}
}
start = 'A'
print(tsp_greedy(G, start))  # Prints (11, [('A', 'D', 1), ('D', 'C', 2), ('C', 'B', 1), ('B', 'E', 4), ('E', 'A', 3)])


# Test case 3: 6 nodes
G = {
    'A': {'B': 3, 'C': 1, 'D': 2, 'E': 5, 'F': 4},
    'B': {'A': 3, 'C': 4, 'D': 6, 'E': 2, 'F': 3},
    'C': {'A': 1, 'B': 4, 'D': 3, 'E': 4, 'F': 2},
    'D': {'A': 2, 'B': 6, 'C': 3, 'E': 1, 'F': 5},
    'E': {'A': 5, 'B': 2, 'C': 4, 'D': 1, 'F': 6},
    'F': {'A': 4, 'B': 3, 'C': 2, 'D': 5, 'E': 6}
}
start = 'A'
print(tsp_greedy(G, start))   # Prints (11, [('A', 'C', 1), ('C', 'F', 2), ('F', 'B', 3), ('B', 'E', 2), ('E', 'D', 1), ('D', 'A', 2)])


# Test case 4: 7 nodes
G = {
    'A': {'B': 4, 'C': 1, 'D': 3, 'E': 7, 'F': 5, 'G': 6},
    'B': {'A': 4, 'C': 6, 'D': 5, 'E': 3, 'F': 2, 'G': 7},
    'C': {'A': 1, 'B': 6, 'D': 4, 'E': 2, 'F': 7, 'G': 3},
    'D': {'A': 3, 'B': 5, 'C': 4, 'E': 6, 'F': 1, 'G': 2},
    'E': {'A': 7, 'B': 3, 'C': 2, 'D': 6, 'F': 4, 'G': 5},
    'F': {'A': 5, 'B': 2, 'C': 7, 'D': 1, 'E': 4, 'G': 6},
    'G': {'A': 6, 'B': 7, 'C': 3, 'D': 2, 'E': 5, 'F': 6}
}
start = 'A'
print(tsp_greedy(G, start))  # Prints (17, [('A', 'C', 1), ('C', 'E', 2), ('E', 'B', 3), ('B', 'F', 2), ('F', 'D', 1), ('D', 'G', 2), ('G', 'A', 6)])


# Test case 5: 8 nodes
G = {
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
print(tsp_greedy(G, start))  # Prints (17, [('A', 'H', 1), ('H', 'B', 2), ('B', 'C', 3), ('C', 'E', 4), ('E', 'F', 1), ('F', 'D', 2), ('D', 'G', 1), ('G', 'A', 3)])