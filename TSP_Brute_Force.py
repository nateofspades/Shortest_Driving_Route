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