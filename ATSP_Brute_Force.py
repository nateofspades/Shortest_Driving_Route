from TSP_Brute_Force import tsp_brute_force
from itertools import permutations
import time


def atsp_brute_force(G, start):
    """
    Computes a minimum-weight Hamiltonian path using brute force, i.e. by calculating all possible Hamiltonian paths of G and extracting one which has the minimum possible weight.
    :param G: A graph which is complete, weighted and undirected.
    :param start: The first node of the Hamiltonian path output.
    :return: A Hamiltonian path of G of minimum weight which begins at the start node, including edge weights and total weight.
    """

    # Get a list of all the nodes.
    nodes = list(G.keys())

    # Initialize variables to store the best cycle and its weight.
    best_cycle = None
    best_cycle_weight = float('inf')

    # Iterate over the permutations of the nodes. We remove start from the nodes list because its location in the permuation is already decided (i.e. at the beginning of the permutation).
    nodes.remove(start)
    for perm in permutations(nodes):
        # Initiate cycle_weight with the weight of the first edge.
        cycle_weight = G[start][perm[0]]
        # Finish the cycle_weight calculation.
        for i in range(len(perm) - 1):
            cycle_weight += G[perm[i]][perm[i + 1]]
        # Update the best cycle and its length if necessary.
        if cycle_weight < best_cycle_weight:
            best_cycle = [(start, perm[0], G[start][perm[0]])] + list(zip(perm, perm[1:], [G[perm[i]][perm[i + 1]] for i in range(len(perm) - 1)]))
            best_cycle_weight = cycle_weight

    return best_cycle_weight, best_cycle


def unit_tests():

    # Unit test 1
    G = {
        'A': {'A': 0, 'B': 2, 'C': 3, 'D': 9},
        'B': {'A': 2, 'B': 0, 'C': 6, 'D': 5},
        'C': {'A': 3, 'B': 6, 'C': 0, 'D': 4},
        'D': {'A': 9, 'B': 5, 'C': 4, 'D': 0}
    }
    start = 'A'
    assert atsp_brute_force(G, start) == (11, [('A', 'B', 2), ('B', 'D', 5), ('D', 'C', 4)])

    # Unit test 2
    G = {
        'A': {'A': 0, 'B': 9, 'C': 6, 'D': 8},
        'B': {'A': 9, 'B': 0, 'C': 3, 'D': 2},
        'C': {'A': 6, 'B': 3, 'C': 0, 'D': 5},
        'D': {'A': 8, 'B': 2, 'C': 5, 'D': 0}
    }
    start = 'A'
    assert atsp_brute_force(G, start) == (11, [('A', 'C', 6), ('C', 'B', 3), ('B', 'D', 2)])

    # Unit test 3
    G = {
        'A': {'A': 0, 'B': 8, 'C': 6, 'D': 3},
        'B': {'A': 8, 'B': 0, 'C': 5, 'D': 5},
        'C': {'A': 6, 'B': 5, 'C': 0, 'D': 1},
        'D': {'A': 3, 'B': 5, 'C': 1, 'D': 0}
    }
    start = 'A'
    assert atsp_brute_force(G, start) == (9, [('A', 'D', 3), ('D', 'C', 1), ('C', 'B', 5)])

    # Unit test 4
    G = {
        'A': {'A': 0, 'B': 2, 'C': 3, 'D': 1},
        'B': {'A': 2, 'B': 0, 'C': 4, 'D': 6},
        'C': {'A': 3, 'B': 4, 'C': 0, 'D': 5},
        'D': {'A': 1, 'B': 6, 'C': 5, 'D': 0}
    }
    start = 'A'
    assert atsp_brute_force(G, start) == (10, [('A', 'D', 1), ('D', 'C', 5), ('C', 'B', 4)])

    # Unit test 5
    G = {
        'A': {'A': 0, 'B': 2, 'C': 4, 'D': 1, 'E': 3},
        'B': {'A': 2, 'B': 0, 'C': 1, 'D': 3, 'E': 4},
        'C': {'A': 4, 'B': 1, 'C': 0, 'D': 2, 'E': 5},
        'D': {'A': 1, 'B': 3, 'C': 2, 'D': 0, 'E': 6},
        'E': {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 0}
    }
    start = 'A'
    assert atsp_brute_force(G, start) == (8, [('A', 'D', 1), ('D', 'C', 2), ('C', 'B', 1), ('B', 'E', 4)])

    # Unit test 6: There are multiple optimal cycles for this test case, so we only test for the total edge weight.
    G = {
        'A': {'A': 0, 'B': 10, 'C': 20, 'D': 30, 'E': 40},
        'B': {'A': 10, 'B': 0, 'C': 15, 'D': 25, 'E': 35},
        'C': {'A': 20, 'B': 15, 'C': 0, 'D': 5, 'E': 15},
        'D': {'A': 30, 'B': 25, 'C': 5, 'D': 0, 'E': 10},
        'E': {'A': 40, 'B': 35, 'C': 15, 'D': 10, 'E': 0}
    }
    start = 'A'
    assert atsp_brute_force(G, start) == (40, [('A', 'B', 10), ('B', 'C', 15), ('C', 'D', 5), ('D', 'E', 10)])

if __name__ == '__main__':
    unit_tests()
    print("All unit tests passed.")