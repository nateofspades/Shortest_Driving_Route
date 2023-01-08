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

G = {
    'A': {'A': 0, 'B': 8, 'C': 6, 'D': 3},
    'B': {'A': 8, 'B': 0, 'C': 5, 'D': 5},
    'C': {'A': 6, 'B': 5, 'C': 0, 'D': 1},
    'D': {'A': 3, 'B': 5, 'C': 1, 'D': 0}
}
print(tsp_brute_force(G, 'A'))


t1 = time.time()
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
print(tsp_brute_force(G, 'A'))
# Prints (279, [('A', 'F', 20), ('F', 'B', 14), ('B', 'E', 17), ('E', 'H', 23), ('H', 'K', 18), ('K', 'C', 11), ('C', 'D', 28), ('D', 'I', 8), ('I', 'G', 12), ('G', 'J', 70), ('J', 'A', 58)])
t2 = time.time()
print("Computing the above output with 11 nodes took ", round(t2-t1, 3), " seconds.")