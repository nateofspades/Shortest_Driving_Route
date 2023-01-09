# This file creates a function that implements Christofide's algorithm for any weighted complete graph that satisfies the triangle inequality.
# The steps in the function definition follow the steps in the Example in this Wikipedia page: https://en.wikipedia.org/wiki/Christofides_algorithm

import networkx as nx

def tsp_christofides(G, start):
    """
    This function implements Christofide's algorithm to generate a Hamiltonian cycle for a weighted complete graph satisfying the triangle inequality.
    It also includes the edge weights in the Hamiltonian cycle, as well as the sum of the edge weights.

    :param G: A dictionary in which the keys are the nodes of a weighted graph, and the value for a node N is a dictionary of all nodes as keys and
              their edge weights with N as values.

    :param start: the first (and last) node in the Hamiltonian cycle; represented as a string.

    :return: a weighted Hamiltonian cycle in G that begins and ends at the start input, as well as the sum of the edge weights; represented as a length-2
        tuple, where the first element is the sum of the edge weights, and the second element is the weighted Hamiltonian cycle, represented as a list of
        length-3 tuples, where the first two elements of a tuple are the two nodes of an edge in the cycle and the third element is the corresponding
        edge weight.
    """

    # Step 1: Convert G to the appropriate format so that it can be used by the networkx library.
    G = convert_graph_to_networkx_form(G)

    # Step 2: Calculate a minimum spanning tree T of G.
    T = nx.minimum_spanning_tree(G)

    # Step 3: Calculate the set of nodes O with odd degree in T.
    T_nodes_and_degrees = T.degree
    O = []
    for node, degree in T_nodes_and_degrees:
        if degree % 2 == 1:
            O.append(node)

    # Step 4: Form the subgraph S of G using only the nodes of O.
    S = nx.induced_subgraph(G, O)

    # Step 5: Construct a minimum-weight perfect matching M in this subgraph S.
    M = nx.min_weight_matching(S)
    M = nx.Graph(M)  # Convert from a set object to a graph object

    # Step 6: Unite matching and spanning tree T ∪ M to form an Eulerian multigraph H; duplicate edges allowed.
    H = nx.MultiGraph(list(T.edges) + list(M.edges))

    # Step 7: Calculate Euler tour in H, beginning and ending at the start node.
    euler_tour = list(nx.eulerian_circuit(H, source=start))

    # Step 8: Remove repeated nodes by creating a list of nodes representing the Hamiltonian cycle.
    hamiltonian_cycle_node_form = []
    hamiltonian_cycle_node_form.append(euler_tour[0][0])
    hamiltonian_cycle_node_form.append(euler_tour[0][1])
    for edge in euler_tour[1:]:
        if edge[1] not in hamiltonian_cycle_node_form:
            hamiltonian_cycle_node_form.append(edge[1])
    # The hamiltonian cycle should end with the same node it started with.
    hamiltonian_cycle_node_form.append(euler_tour[0][0])

    # Step 9: Combine the nodes back into tuples to represent the Hamiltonian cycle as a list of edges.
    #         Moreover, include the weight of each edge, and compute the sum of the edge weights of the cycle
    hamiltonian_cycle_weighted_edge_form = []
    total_edge_weight = 0
    n = len(hamiltonian_cycle_node_form)
    for i in range(n - 1):
        node_1 = hamiltonian_cycle_node_form[i]
        node_2 = hamiltonian_cycle_node_form[i + 1]
        weight = G.edges[node_1, node_2]['weight']
        hamiltonian_cycle_weighted_edge_form.append((node_1, node_2, weight))
        total_edge_weight += weight

    return total_edge_weight, hamiltonian_cycle_weighted_edge_form

def convert_graph_to_networkx_form(G):
    """
    This is a helper function for tsp_christofides(). It converts the input graph G into a format that allows it to be input into various networkx functions.

    :param G: A dictionary in which the keys are the nodes of a weighted graph,
              and the value for a node N is a dictionary of all nodes as keys and their edge weights with N as values.

    :return: A networkx graph object.
    """

    # Convert G to a list of length-3 tuples, where the first two elements of a tuple are nodes of G and the third is the weight of the edge joining these nodes.
    G_list_form = []
    for key1, value1 in G.items():
        for key2, value2 in value1.items():
            if key1 < key2:
                G_list_form.append((key1, key2, value2))

    # Convert G to a networkx graph object.
    G_networkx_form = []
    for edge in G_list_form:
        G_networkx_form.append((edge[0], edge[1], {'weight': edge[2]}))
    G_networkx_form = nx.Graph(G_networkx_form)

    return G_networkx_form


def unit_tests():
    """
    A Hamiltonian cycle was computed by hand using Christofides algorithm for some graphs on 4 nodes and 5 nodes.
    These by-hand computations are compared to the outputs of tsp_christofides(). Note that the algorithm is not
    deterministic; it can output different cycles, so a failure of the unit tests does not imply a failure of code.
    """

    # Unit test 1
    G = {
        'A': {'A': 0, 'B': 2, 'C': 3, 'D': 9},
        'B': {'A': 2, 'B': 0, 'C': 6, 'D': 5},
        'C': {'A': 3, 'B': 6, 'C': 0, 'D': 4},
        'D': {'A': 9, 'B': 5, 'C': 4, 'D': 0}
    }
    start = 'A'
    assert tsp_christofides(G, start) == (14, [('A', 'C', 3), ('C', 'D', 4), ('D', 'B', 5), ('B', 'A', 2)])

    # Unit test 2
    G = {
        'A': {'A': 0, 'B': 9, 'C': 6, 'D': 8},
        'B': {'A': 9, 'B': 0, 'C': 3, 'D': 2},
        'C': {'A': 6, 'B': 3, 'C': 0, 'D': 5},
        'D': {'A': 8, 'B': 2, 'C': 5, 'D': 0}
    }
    start = 'A'
    assert tsp_christofides(G, start) == (19, [('A', 'D', 8), ('D', 'B', 2), ('B', 'C', 3), ('C', 'A', 6)])

    # Unit test 3
    G = {
        'A': {'A': 0, 'B': 8, 'C': 6, 'D': 3},
        'B': {'A': 8, 'B': 0, 'C': 5, 'D': 5},
        'C': {'A': 6, 'B': 5, 'C': 0, 'D': 1},
        'D': {'A': 3, 'B': 5, 'C': 1, 'D': 0}
    }
    start = 'A'
    assert tsp_christofides(G, start) == (17, [('A', 'B', 8), ('B', 'C', 5), ('C', 'D', 1), ('D', 'A', 3)])

    # Unit test 4
    G = {
        'A': {'A': 0, 'B': 2, 'C': 3, 'D': 1},
        'B': {'A': 2, 'B': 0, 'C': 4, 'D': 6},
        'C': {'A': 3, 'B': 4, 'C': 0, 'D': 5},
        'D': {'A': 1, 'B': 6, 'C': 5, 'D': 0}
    }
    start = 'A'
    assert tsp_christofides(G, start) == (14, [('A', 'C', 3), ('C', 'B', 4), ('B', 'D', 6), ('D', 'A', 1)])

    # Unit test 5
    G = {
        'A': {'A': 0, 'B': 2, 'C': 4, 'D': 1, 'E': 3},
        'B': {'A': 2, 'B': 0, 'C': 1, 'D': 3, 'E': 4},
        'C': {'A': 4, 'B': 1, 'C': 0, 'D': 2, 'E': 5},
        'D': {'A': 1, 'B': 3, 'C': 2, 'D': 0, 'E': 6},
        'E': {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 0}
    }
    start = 'A'
    assert tsp_christofides(G, start) == (11, [('A', 'E', 3), ('E', 'B', 4), ('B', 'C', 1), ('C', 'D', 2), ('D', 'A', 1)])

    # Unit test 6
    G = {
        'A': {'A': 0, 'B': 10, 'C': 20, 'D': 30, 'E': 40},
        'B': {'A': 10, 'B': 0, 'C': 15, 'D': 25, 'E': 35},
        'C': {'A': 20, 'B': 15, 'C': 0, 'D': 5, 'E': 15},
        'D': {'A': 30, 'B': 25, 'C': 5, 'D': 0, 'E': 10},
        'E': {'A': 40, 'B': 35, 'C': 15, 'D': 10, 'E': 0}
    }
    start = 'A'
    assert tsp_christofides(G, start) == (80, [('A', 'E', 40), ('E', 'D', 10), ('D', 'C', 5), ('C', 'B', 15), ('B', 'A', 10)])

    # Unit test 7
    G = {
        'A': {'A': 0, 'B': 12, 'C': 3, 'D': 6, 'E': 8},
        'B': {'A': 12, 'B': 0, 'C': 4, 'D': 4, 'E': 5},
        'C': {'A': 3, 'B': 4, 'C': 0, 'D': 9, 'E': 1},
        'D': {'A': 6, 'B': 4, 'C': 9, 'D': 0, 'E': 4},
        'E': {'A': 8, 'B': 5, 'C': 1, 'D': 4, 'E': 0},
    }
    start = 'A'
    assert tsp_christofides(G, start) == (23, [('A', 'D', 6), ('D', 'B', 4), ('B', 'C', 4), ('C', 'E', 1), ('E', 'A', 8)])

if __name__ == '__main__':
    unit_tests()
    print("All unit tests passed.")