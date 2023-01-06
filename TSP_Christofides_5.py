# This file creates a function that implements Christofide's algorithm for any weighted complete graph that satisfies the triangle inequality.
# The steps in the function definition follow the steps in the Example in this Wikipedia page: https://en.wikipedia.org/wiki/Christofides_algorithm

import networkx as nx

def christofides_algorithm(G, start):
    """
    This function implements Christofide's algorithm to generate a Hamiltonian cycle for a weighted complete graph satisfying the triangle inequality.
    It also includes the edge weights in the Hamiltonian cycle, as well as the sum of the edge weights.

    :param G: a weighted complete graph satisfying the triangle inequality; represented as a list of length-3 tuples, where the first two elements of a
        tuple are the two endpoints of an edge in G and the third element is the corresponding edge weight.

    :param start: the first (and last) node in the Hamiltonian cycle; represented as a string.

    :return: a weighted Hamiltonian cycle in G that begins and ends at the start input, as well as the sum of the edge weights; represented as a length-2
        tuple, where the first element is the sum of the edge weights, and the second element is the weighted Hamiltonian cycle, represented similarly as G
        is (i.e. as a list of length-3 tuples, where the first two elements of a tuple are the two endpoints of an edge in the cycle and the third element
        is the corresponding edge weight).
    """

    # Step 1: Convert G to the appropriate format so that it can be used by the networkx library.
    G_temp = []
    for edge in G:
        G_temp.append((edge[0], edge[1], {'weight': edge[2]}))
    G = nx.Graph(G_temp)

    # Step 2: Calculate minimum spanning tree T of G.
    T = nx.minimum_spanning_tree(G)

    # Step 3: Calculate the set of vertices O with odd degree in T.


    # Step 4: Form the subgraph of G using only the vertices of O.

    # Step 5: Construct a minimum-weight perfect matching M in this subgraph

    # Step 6: Unite matching and spanning tree T ∪ M to form an Eulerian multigraph H; unions the edge sets and vertex sets

    # Step 7: Calculate Euler tour in H

    # Step 8: Remove repeated vertices

    # Step 9: (NOT FROM WIKI PAGE: NEED TO INCLUDE WEIGHTS BACK IN PLUS ADD TOTAL WEIGHT)