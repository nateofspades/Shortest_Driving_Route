def tsp_greedy(G, start):
    """
    Computes a Hamiltonian cycle using a greedy approach, i.e. where each node after the first is selected by considering
    all yet-unvisited nodes in the graph and selecting one which has the minimum edge weight with the current node. Once
    all nodes have been visited, the last node is then joined with the start node.
    :param G: A graph which is complete, weighted and undirected.
    :param start: The first (and last) node of the Hamiltonian cycle output.
    :return: A Hamiltonian cycle of G produced by the greedy approach, including edge weights and total weight.
    """

    # We need to keep track of which nodes have already been visited and which node we are currently at.
    visited_nodes = []
    current_node = start

    # The outputs of the function.
    cycle_weight = 0
    cycle = []

    # Visit all nodes in the graph.
    while len(visited_nodes) < len(G):
        visited_nodes.append(current_node)
        min_weight = float('inf')
        next_node = None

        # Find the closest unvisited node.
        for node, weight in G[current_node].items():
            if node not in visited_nodes and weight < min_weight:
                min_weight = weight
                next_node = node

        # Add the edge to the cycle and update the total weight if a next node was found.
        if next_node is not None:
            cycle.append((current_node, next_node, min_weight))
            cycle_weight += min_weight
            current_node = next_node

    # Return to the start node.
    cycle.append((current_node, start, G[current_node][start]))
    cycle_weight += G[current_node][start]

    return cycle_weight, cycle


def unit_tests():
    """
    A Hamiltonian cycle was computed by hand using a greedy approach for graphs of various sizes. These by-hand computations
    are compared to the outputs of tsp_greedy(). Note that the greedy approach is not deterministic because sometimes the
    current node has 2 or more available adjacent nodes which both have the same minimum edge weight. The greedy approach can
    output different cycles, so a failure of the unit tests does not imply a failure of code.
    """
    # Unit test 1
    G = {
        'A': {'A': 0, 'B': 2, 'C': 3, 'D': 9},
        'B': {'A': 2, 'B': 0, 'C': 6, 'D': 5},
        'C': {'A': 3, 'B': 6, 'C': 0, 'D': 4},
        'D': {'A': 9, 'B': 5, 'C': 4, 'D': 0}
    }
    start = 'A'
    assert tsp_greedy(G, start) == (14, [('A', 'B', 2), ('B', 'D', 5), ('D', 'C', 4), ('C', 'A', 3)])

    # Unit test 2
    G = {
        'A': {'A': 0, 'B': 9, 'C': 6, 'D': 8},
        'B': {'A': 9, 'B': 0, 'C': 3, 'D': 2},
        'C': {'A': 6, 'B': 3, 'C': 0, 'D': 5},
        'D': {'A': 8, 'B': 2, 'C': 5, 'D': 0}
    }
    start = 'A'
    assert tsp_greedy(G, start) == (19, [('A', 'C', 6), ('C', 'B', 3), ('B', 'D', 2), ('D', 'A', 8)])

    # Unit test 3
    G = {
        'A': {'A': 0, 'B': 8, 'C': 6, 'D': 3},
        'B': {'A': 8, 'B': 0, 'C': 5, 'D': 5},
        'C': {'A': 6, 'B': 5, 'C': 0, 'D': 1},
        'D': {'A': 3, 'B': 5, 'C': 1, 'D': 0}
    }
    start = 'A'
    assert tsp_greedy(G, start) == (17, [('A', 'D', 3), ('D', 'C', 1), ('C', 'B', 5), ('B', 'A', 8)])

    # Unit test 4
    G = {
        'A': {'A': 0, 'B': 2, 'C': 3, 'D': 1},
        'B': {'A': 2, 'B': 0, 'C': 4, 'D': 6},
        'C': {'A': 3, 'B': 4, 'C': 0, 'D': 5},
        'D': {'A': 1, 'B': 6, 'C': 5, 'D': 0}
    }
    start = 'A'
    assert tsp_greedy(G, start) == (12, [('A', 'D', 1), ('D', 'C', 5), ('C', 'B', 4), ('B', 'A', 2)])

    # Unit test 5
    G = {
        'A': {'A': 0, 'B': 2, 'C': 4, 'D': 1, 'E': 3},
        'B': {'A': 2, 'B': 0, 'C': 1, 'D': 3, 'E': 4},
        'C': {'A': 4, 'B': 1, 'C': 0, 'D': 2, 'E': 5},
        'D': {'A': 1, 'B': 3, 'C': 2, 'D': 0, 'E': 6},
        'E': {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 0}
    }
    start = 'A'
    assert tsp_greedy(G, start) == (11, [('A', 'D', 1), ('D', 'C', 2), ('C', 'B', 1), ('B', 'E', 4), ('E', 'A', 3)])

    # Unit test 6
    G = {
        'A': {'A': 0, 'B': 10, 'C': 20, 'D': 30, 'E': 40},
        'B': {'A': 10, 'B': 0, 'C': 15, 'D': 25, 'E': 35},
        'C': {'A': 20, 'B': 15, 'C': 0, 'D': 5, 'E': 15},
        'D': {'A': 30, 'B': 25, 'C': 5, 'D': 0, 'E': 10},
        'E': {'A': 40, 'B': 35, 'C': 15, 'D': 10, 'E': 0}
    }
    start = 'A'
    assert tsp_greedy(G, start) == (80, [('A', 'B', 10), ('B', 'C', 15), ('C', 'D', 5), ('D', 'E', 10), ('E', 'A', 40)])

    # Unit test 7
    G = {
        'A': {'A': 0, 'B': 12, 'C': 3, 'D': 6, 'E': 8},
        'B': {'A': 12, 'B': 0, 'C': 4, 'D': 4, 'E': 5},
        'C': {'A': 3, 'B': 4, 'C': 0, 'D': 9, 'E': 1},
        'D': {'A': 6, 'B': 4, 'C': 9, 'D': 0, 'E': 4},
        'E': {'A': 8, 'B': 5, 'C': 1, 'D': 4, 'E': 0},
    }
    start = 'A'
    assert tsp_greedy(G, start) == (24, [('A', 'C', 3), ('C', 'E', 1), ('E', 'D', 4), ('D', 'B', 4), ('B', 'A', 12)])

    # Unit test 8
    G = {
        'A': {'A': 0, 'B': 3, 'C': 1, 'D': 2, 'E': 5, 'F': 4},
        'B': {'A': 3, 'B': 0, 'C': 4, 'D': 6, 'E': 2, 'F': 3},
        'C': {'A': 1, 'B': 4, 'C': 0, 'D': 3, 'E': 4, 'F': 2},
        'D': {'A': 2, 'B': 6, 'C': 3, 'D': 0, 'E': 1, 'F': 5},
        'E': {'A': 5, 'B': 2, 'C': 4, 'D': 1, 'E': 0, 'F': 6},
        'F': {'A': 4, 'B': 3, 'C': 2, 'D': 5, 'E': 6, 'F': 0}
    }
    start = 'A'
    assert tsp_greedy(G, start) == (11, [('A', 'C', 1), ('C', 'F', 2), ('F', 'B', 3), ('B', 'E', 2), ('E', 'D', 1), ('D', 'A', 2)])

    # Unit test 9
    G = {
        'A': {'A': 0, 'B': 4, 'C': 1, 'D': 3, 'E': 7, 'F': 5, 'G': 6},
        'B': {'A': 4, 'B': 0, 'C': 6, 'D': 5, 'E': 3, 'F': 2, 'G': 7},
        'C': {'A': 1, 'B': 6, 'C': 0, 'D': 4, 'E': 2, 'F': 7, 'G': 3},
        'D': {'A': 3, 'B': 5, 'C': 4, 'D': 0, 'E': 6, 'F': 1, 'G': 2},
        'E': {'A': 7, 'B': 3, 'C': 2, 'D': 6, 'E': 0, 'F': 4, 'G': 5},
        'F': {'A': 5, 'B': 2, 'C': 7, 'D': 1, 'E': 4, 'F': 0, 'G': 6},
        'G': {'A': 6, 'B': 7, 'C': 3, 'D': 2, 'E': 5, 'F': 6, 'G': 0}
    }
    start = 'A'
    assert tsp_greedy(G, start) == (17, [('A', 'C', 1), ('C', 'E', 2), ('E', 'B', 3), ('B', 'F', 2), ('F', 'D', 1), ('D', 'G', 2), ('G', 'A', 6)])

    # Unit test 10
    G = {
        'A': {'A': 0, 'B': 5, 'C': 2, 'D': 4, 'E': 8, 'F': 7, 'G': 3, 'H': 1},
        'B': {'A': 5, 'B': 0, 'C': 3, 'D': 7, 'E': 5, 'F': 6, 'G': 4, 'H': 2},
        'C': {'A': 2, 'B': 3, 'C': 0, 'D': 6, 'E': 4, 'F': 5, 'G': 7, 'H': 8},
        'D': {'A': 4, 'B': 7, 'C': 6, 'D': 0, 'E': 3, 'F': 2, 'G': 1, 'H': 5},
        'E': {'A': 8, 'B': 5, 'C': 4, 'D': 3, 'E': 0, 'F': 1, 'G': 6, 'H': 7},
        'F': {'A': 7, 'B': 6, 'C': 5, 'D': 2, 'E': 1, 'F': 0, 'G': 8, 'H': 3},
        'G': {'A': 3, 'B': 4, 'C': 7, 'D': 1, 'E': 6, 'F': 8, 'G': 0, 'H': 4},
        'H': {'A': 1, 'B': 2, 'C': 8, 'D': 5, 'E': 7, 'F': 3, 'G': 4, 'H': 0}
    }
    start = 'A'
    assert tsp_greedy(G, start) == (17, [('A', 'H', 1), ('H', 'B', 2), ('B', 'C', 3), ('C', 'E', 4), ('E', 'F', 1), ('F', 'D', 2), ('D', 'G', 1), ('G', 'A', 3)])

    # Unit test 11
    G = {
        'A': {'A': 0, 'B': 3, 'C': 7, 'D': 5, 'E': 4, 'F': 9, 'G': 8, 'H': 2, 'I': 1},
        'B': {'A': 3, 'B': 0, 'C': 6, 'D': 4, 'E': 5, 'F': 8, 'G': 7, 'H': 1, 'I': 2},
        'C': {'A': 7, 'B': 6, 'C': 0, 'D': 8, 'E': 7, 'F': 2, 'G': 1, 'H': 5, 'I': 4},
        'D': {'A': 5, 'B': 4, 'C': 8, 'D': 0, 'E': 9, 'F': 1, 'G': 2, 'H': 6, 'I': 3},
        'E': {'A': 4, 'B': 5, 'C': 7, 'D': 9, 'E': 0, 'F': 3, 'G': 4, 'H': 7, 'I': 6},
        'F': {'A': 9, 'B': 8, 'C': 2, 'D': 1, 'E': 3, 'F': 0, 'G': 5, 'H': 8, 'I': 7},
        'G': {'A': 8, 'B': 7, 'C': 1, 'D': 2, 'E': 4, 'F': 5, 'G': 0, 'H': 9, 'I': 8},
        'H': {'A': 2, 'B': 1, 'C': 5, 'D': 6, 'E': 7, 'F': 8, 'G': 9, 'H': 0, 'I': 9},
        'I': {'A': 1, 'B': 2, 'C': 4, 'D': 3, 'E': 6, 'F': 7, 'G': 8, 'H': 9, 'I': 0}
    }
    start = 'A'
    assert tsp_greedy(G, start) == (20, [('A', 'I', 1), ('I', 'B', 2), ('B', 'H', 1), ('H', 'C', 5), ('C', 'G', 1), ('G', 'D', 2), ('D', 'F', 1), ('F', 'E', 3), ('E', 'A', 4)])

    # Unit test 12
    G = {
        'A': {'A': 0, 'B': 12, 'C': 3, 'D': 6, 'E': 8, 'F': 7, 'G': 9, 'H': 1, 'I': 13, 'J': 8},
        'B': {'A': 12, 'B': 0, 'C': 2, 'D': 2, 'E': 9, 'F': 14, 'G': 17, 'H': 6, 'I': 3, 'J': 4},
        'C': {'A': 3, 'B': 2, 'C': 0, 'D': 1, 'E': 5, 'F': 5, 'G': 2, 'H': 4, 'I': 1, 'J': 7},
        'D': {'A': 6, 'B': 2, 'C': 1, 'D': 0, 'E': 3, 'F': 3, 'G': 10, 'H': 19, 'I': 20, 'J': 28},
        'E': {'A': 8, 'B': 9, 'C': 5, 'D': 3, 'E': 0, 'F': 4, 'G': 11, 'H': 14, 'I': 8, 'J': 1},
        'F': {'A': 7, 'B': 14, 'C': 5, 'D': 3, 'E': 4, 'F': 0, 'G': 12, 'H': 1, 'I': 1, 'J': 2},
        'G': {'A': 9, 'B': 17, 'C': 2, 'D': 10, 'E': 11, 'F': 12, 'G': 0, 'H': 13, 'I': 16, 'J': 18},
        'H': {'A': 1, 'B': 6, 'C': 4, 'D': 19, 'E': 14, 'F': 1, 'G': 13, 'H': 13, 'I': 6, 'J': 8},
        'I': {'A': 13, 'B': 3, 'C': 1, 'D': 20, 'E': 8, 'F': 1, 'G': 16, 'H': 6, 'I': 0, 'J': 2},
        'J': {'A': 8, 'B': 4, 'C': 7, 'D': 28, 'E': 1, 'F': 2, 'G': 18, 'H': 8, 'I': 2, 'J': 0}
    }
    start = 'A'
    assert tsp_greedy(G, start) == (32, [('A', 'H', 1), ('H', 'F', 1), ('F', 'I', 1), ('I', 'C', 1), ('C', 'D', 1), ('D', 'B', 2), ('B', 'J', 4), ('J', 'E', 1), ('E', 'G', 11), ('G', 'A', 9)])

    # Unit test 13
    G = {
        'A': {'A': 0, 'B': 37, 'C': 85, 'D': 64, 'E': 81, 'F': 20, 'G': 63, 'H': 97, 'I': 20, 'J': 58, 'K': 91},
        'B': {'A': 37, 'B': 0, 'C': 97, 'D': 44, 'E': 17, 'F': 14, 'G': 58, 'H': 72, 'I': 54, 'J': 67, 'K': 75},
        'C': {'A': 85, 'B': 97, 'C': 0, 'D': 28, 'E': 40, 'F': 39, 'G': 51, 'H': 79, 'I': 44, 'J': 60, 'K': 11},
        'D': {'A': 64, 'B': 44, 'C': 28, 'D': 0, 'E': 39, 'F': 7, 'G': 84, 'H': 67, 'I': 8, 'J': 66, 'K': 95},
        'E': {'A': 81, 'B': 17, 'C': 40, 'D': 39, 'E': 0, 'F': 29, 'G': 44, 'H': 23, 'I': 4, 'J': 79, 'K': 71},
        'F': {'A': 20, 'B': 14, 'C': 39, 'D': 7, 'E': 29, 'F': 0, 'G': 23, 'H': 75, 'I': 65, 'J': 97, 'K': 54},
        'G': {'A': 63, 'B': 58, 'C': 51, 'D': 84, 'E': 44, 'F': 23, 'G': 0, 'H': 97, 'I': 12, 'J': 70, 'K': 96},
        'H': {'A': 97, 'B': 72, 'C': 79, 'D': 67, 'E': 23, 'F': 75, 'G': 97, 'H': 0, 'I': 25, 'J': 65, 'K': 18},
        'I': {'A': 20, 'B': 54, 'C': 44, 'D': 8, 'E': 4, 'F': 65, 'G': 12, 'H': 25, 'I': 0, 'J': 88, 'K': 56},
        'J': {'A': 58, 'B': 67, 'C': 60, 'D': 66, 'E': 79, 'F': 97, 'G': 70, 'H': 65, 'I': 88, 'J': 0, 'K': 89},
        'K': {'A': 91, 'B': 75, 'C': 11, 'D': 95, 'E': 71, 'F': 54, 'G': 96, 'H': 18, 'I': 56, 'J': 89, 'K': 0}
    }
    start = 'A'
    assert tsp_greedy(G, start) == (317, [('A', 'F', 20), ('F', 'D', 7), ('D', 'I', 8), ('I', 'E', 4), ('E', 'B', 17), ('B', 'G', 58), ('G', 'C', 51), ('C', 'K', 11), ('K', 'H', 18), ('H', 'J', 65), ('J', 'A', 58)])

if __name__ == '__main__':
    unit_tests()
    print("All unit tests passed.")