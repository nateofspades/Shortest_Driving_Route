from TSP_Christofides import tsp_christofides

def atsp_christofides(G, start):
    """
     Computes a Hamiltonian path using Christofide's algorith, i.e. by using Christofides algorithm to generate a Hamiltonian
     cycle, and then the last edge is removed.
     :param G: A graph which is complete, weighted and undirected.
     :param start: The first node of the Hamiltonian path output.
     :return: A Hamiltonian path of G produced by Christofide's algorithm, including edge weights and total weight.
     """

    # Use tsp_christofides() to extract a weighted Hamiltonian cycle and its total weight.
    cycle_and_weight = tsp_christofides(G, start)
    cycle = cycle_and_weight[1]
    cycle_weight = cycle_and_weight[0]

    # Remove the last edge from the cycle, as well as its weight from the total weight.
    path = cycle[:-1]
    last_edge_weight = cycle[-1][2]
    path_weight = cycle_weight - last_edge_weight

    return path_weight, path


def unit_tests():

    # Unit test 1
    G = {
        'A': {'A': 0, 'B': 2, 'C': 3, 'D': 9},
        'B': {'A': 2, 'B': 0, 'C': 6, 'D': 5},
        'C': {'A': 3, 'B': 6, 'C': 0, 'D': 4},
        'D': {'A': 9, 'B': 5, 'C': 4, 'D': 0}
    }
    start = 'A'
    assert atsp_christofides(G, start) == (12, [('A', 'C', 3), ('C', 'D', 4), ('D', 'B', 5)])

    # Unit test 2
    G = {
        'A': {'A': 0, 'B': 9, 'C': 6, 'D': 8},
        'B': {'A': 9, 'B': 0, 'C': 3, 'D': 2},
        'C': {'A': 6, 'B': 3, 'C': 0, 'D': 5},
        'D': {'A': 8, 'B': 2, 'C': 5, 'D': 0}
    }
    start = 'A'
    assert atsp_christofides(G, start) == (13, [('A', 'D', 8), ('D', 'B', 2), ('B', 'C', 3)])

    # Unit test 3
    G = {
        'A': {'A': 0, 'B': 8, 'C': 6, 'D': 3},
        'B': {'A': 8, 'B': 0, 'C': 5, 'D': 5},
        'C': {'A': 6, 'B': 5, 'C': 0, 'D': 1},
        'D': {'A': 3, 'B': 5, 'C': 1, 'D': 0}
    }
    start = 'A'
    assert atsp_christofides(G, start) == (14, [('A', 'B', 8), ('B', 'C', 5), ('C', 'D', 1)])

    # Unit test 4
    G = {
        'A': {'A': 0, 'B': 2, 'C': 3, 'D': 1},
        'B': {'A': 2, 'B': 0, 'C': 4, 'D': 6},
        'C': {'A': 3, 'B': 4, 'C': 0, 'D': 5},
        'D': {'A': 1, 'B': 6, 'C': 5, 'D': 0}
    }
    start = 'A'
    assert atsp_christofides(G, start) == (13, [('A', 'C', 3), ('C', 'B', 4), ('B', 'D', 6)])

    # Unit test 5
    G = {
        'A': {'A': 0, 'B': 2, 'C': 4, 'D': 1, 'E': 3},
        'B': {'A': 2, 'B': 0, 'C': 1, 'D': 3, 'E': 4},
        'C': {'A': 4, 'B': 1, 'C': 0, 'D': 2, 'E': 5},
        'D': {'A': 1, 'B': 3, 'C': 2, 'D': 0, 'E': 6},
        'E': {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 0}
    }
    start = 'A'
    assert atsp_christofides(G, start) == (10, [('A', 'E', 3), ('E', 'B', 4), ('B', 'C', 1), ('C', 'D', 2)])

    # Unit test 6
    G = {
        'A': {'A': 0, 'B': 10, 'C': 20, 'D': 30, 'E': 40},
        'B': {'A': 10, 'B': 0, 'C': 15, 'D': 25, 'E': 35},
        'C': {'A': 20, 'B': 15, 'C': 0, 'D': 5, 'E': 15},
        'D': {'A': 30, 'B': 25, 'C': 5, 'D': 0, 'E': 10},
        'E': {'A': 40, 'B': 35, 'C': 15, 'D': 10, 'E': 0}
    }
    start = 'A'
    assert atsp_christofides(G, start) == (70, [('A', 'E', 40), ('E', 'D', 10), ('D', 'C', 5), ('C', 'B', 15)])

    # Unit test 7
    G = {
        'A': {'A': 0, 'B': 12, 'C': 3, 'D': 6, 'E': 8},
        'B': {'A': 12, 'B': 0, 'C': 4, 'D': 4, 'E': 5},
        'C': {'A': 3, 'B': 4, 'C': 0, 'D': 9, 'E': 1},
        'D': {'A': 6, 'B': 4, 'C': 9, 'D': 0, 'E': 4},
        'E': {'A': 8, 'B': 5, 'C': 1, 'D': 4, 'E': 0},
    }
    start = 'A'
    assert atsp_christofides(G, start) == (15, [('A', 'D', 6), ('D', 'B', 4), ('B', 'C', 4), ('C', 'E', 1)])

if __name__ == '__main__':
    unit_tests()
    print("All unit tests passed.")