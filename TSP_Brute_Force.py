from itertools import permutations
import time

def tsp_brute_force(G, start):
    # Get a list of all the nodes
    nodes = list(G.keys())

    # Initialize variables to store the best cycle and its length.
    best_cycle = None
    best_cycle_length = float('inf')

    # Iterate over the permutations of the nodes.
    node_permutation_list = generate_permutations(G, start)
    for perm in node_permutation_list:
        # Calculate the length of the cycle
        cycle_length = 0
        for i in range(len(perm) - 1):
            cycle_length += G[perm[i]][perm[i + 1]]
        # Add the cost of going from the last node back to the start node
        cycle_length += G[perm[-1]][start]
        # Update the best cycle and its length if necessary
        if cycle_length < best_cycle_length:
            best_cycle = list(zip(perm, perm[1:] + (start,), [G[perm[i]][perm[i + 1]] for i in range(len(perm) - 1)] + [G[perm[-1]][start]]))
            best_cycle_length = cycle_length

    return best_cycle_length, best_cycle

def generate_permutations(G, start):
    """
    This generates all permutations of the nodes of G corresponding to cycles which begin at start, but with reversals omitted.
    For example, if G has nodes "A", "B", "C", "D" and start="A", the output list would include permutation ["A", "B", "C", "D"]
    (corresponding to cycle ABCDA) but the output list would not include ["A", "D", "C", "B"] (corresponding to cycle ADCBA).
    This is because ADCBA is the reversal of ABCDA, so they're essentially the same cycle and need not be considered twice when
    searching for a minimum-weight Hamiltonian cycle.
    :param G:
    :param start:
    :return: A list of tuples of nodes, where each tuple of nodes represents a Hamiltonian cycle in G beginning at the start input.
    """
    nodes = list(G.keys())
    nodes.remove(start)
    permutation_list = []
    for perm in permutations(nodes):
        if perm <= perm[::-1]:
            permutation_list.append(tuple([start] + list(perm)))
    return permutation_list

# Unit tests
def unit_tests():
    """
    A minimum total edge weight Hamiltonian cycle was computed by hand for some graphs on 4 nodes and 5 nodes.
    These by-hand computations are compared to the outputs of tsp_brute_force().
    """

    # Unit test 1
    G = {
        'A': {'A': 0, 'B': 2, 'C': 3, 'D': 9},
        'B': {'A': 2, 'B': 0, 'C': 6, 'D': 5},
        'C': {'A': 3, 'B': 6, 'C': 0, 'D': 4},
        'D': {'A': 9, 'B': 5, 'C': 4, 'D': 0}
    }
    start = 'A'
    assert tsp_brute_force(G, start) == (14, [('A', 'B', 2), ('B', 'D', 5), ('D', 'C', 4), ('C', 'A', 3)])

    # Unit test 2
    G = {
        'A': {'A': 0, 'B': 9, 'C': 6, 'D': 8},
        'B': {'A': 9, 'B': 0, 'C': 3, 'D': 2},
        'C': {'A': 6, 'B': 3, 'C': 0, 'D': 5},
        'D': {'A': 8, 'B': 2, 'C': 5, 'D': 0}
    }
    start = 'A'
    assert tsp_brute_force(G, start) == (19, [('A', 'C', 6), ('C', 'B', 3), ('B', 'D', 2), ('D', 'A', 8)])

    # Unit test 3
    G = {
        'A': {'A': 0, 'B': 8, 'C': 6, 'D': 3},
        'B': {'A': 8, 'B': 0, 'C': 5, 'D': 5},
        'C': {'A': 6, 'B': 5, 'C': 0, 'D': 1},
        'D': {'A': 3, 'B': 5, 'C': 1, 'D': 0}
    }
    start = 'A'
    assert tsp_brute_force(G, start) == (17, [('A', 'B', 8), ('B', 'C', 5), ('C', 'D', 1), ('D', 'A', 3)])

    # Unit test 4
    G = {
        'A': {'A': 0, 'B': 2, 'C': 3, 'D': 1},
        'B': {'A': 2, 'B': 0, 'C': 4, 'D': 6},
        'C': {'A': 3, 'B': 4, 'C': 0, 'D': 5},
        'D': {'A': 1, 'B': 6, 'C': 5, 'D': 0}
    }
    start = 'A'
    assert tsp_brute_force(G, start) == (12, [('A', 'B', 2), ('B', 'C', 4), ('C', 'D', 5), ('D', 'A', 1)])

    # Unit test 5
    G = {
        'A': {'A': 0, 'B': 2, 'C': 4, 'D': 1, 'E': 3},
        'B': {'A': 2, 'B': 0, 'C': 1, 'D': 3, 'E': 4},
        'C': {'A': 4, 'B': 1, 'C': 0, 'D': 2, 'E': 5},
        'D': {'A': 1, 'B': 3, 'C': 2, 'D': 0, 'E': 6},
        'E': {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 0}
    }
    start = 'A'
    assert tsp_brute_force(G, start) == (11, [('A', 'D', 1), ('D', 'C', 2), ('C', 'B', 1), ('B', 'E', 4), ('E', 'A', 3)])

    # Unit test 6: There are multiple optimal cycles for this test case, so we only test for the total edge weight.
    G = {
        'A': {'A': 0, 'B': 10, 'C': 20, 'D': 30, 'E': 40},
        'B': {'A': 10, 'B': 0, 'C': 15, 'D': 25, 'E': 35},
        'C': {'A': 20, 'B': 15, 'C': 0, 'D': 5, 'E': 15},
        'D': {'A': 30, 'B': 25, 'C': 5, 'D': 0, 'E': 10},
        'E': {'A': 40, 'B': 35, 'C': 15, 'D': 10, 'E': 0}
    }
    start = 'A'
    assert tsp_brute_force(G, start)[0] == 80

if __name__ == '__main__':
    unit_tests()
    print("All unit tests passed.")