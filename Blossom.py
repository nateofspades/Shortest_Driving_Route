from collections import defaultdict

def blossom(graph, match, start, visited):
    visited[start] = True
    for neighbor in graph[start]:
        if neighbor not in visited:
            if match[neighbor] == -1 or blossom(graph, match, match[neighbor], visited):
                match[neighbor] = start
                return True
    return False

def find_matching(graph, n):
    match = [-1] * n
    for i in range(n):
        if match[i] == -1:
            blossom(graph, match, i, defaultdict(bool))
    return match

# Example usage

graph = {'A': {'B': 1, 'C': 4, 'D': 3},
         'B': {'A': 1, 'C': 2, 'D': 5},
         'C': {'A': 4, 'B': 2, 'D': 6},
         'D': {'A': 3, 'B': 5, 'C': 6}}

# Convert node labels to integers
int_graph = {}
for i, node in enumerate(graph):
    int_graph[i] = {int(neighbor): weight for neighbor, weight in graph[node].items()}

matching = find_matching(int_graph, 4)
print(matching)