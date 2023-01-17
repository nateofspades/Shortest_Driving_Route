from TSP_Brute_Force import tsp_brute_force
from TSP_Greedy import tsp_greedy
from TSP_Christofides import tsp_christofides

def tsp(G, start, max_brute_force_n = 11):

    nodes = list(G.keys())
    n = len(nodes)
    nodes.remove(start)

    # If G has 2 nodes then there is just one possible Hamiltonian cycle, which is hardcoded below.
    if n == 2:
        second_node = nodes[0]
        cycle = [(start, second_node, G[start][second_node]), (second_node, start, G[second_node][start])]
        cycle_weight = G[start][second_node] + G[second_node][start]
        return cycle_weight, cycle

    # If G has 3 nodes then there are just two possible Hamiltonian cycles, and they are essentially the same, just in
    # reverse relative to each other. It doesn't matter which is selected, so one of them is hardcoded below.
    if n == 3:
        second_node = nodes[0]
        third_node = nodes[1]
        cycle = [(start, second_node, G[start][second_node]), (second_node, third_node, G[second_node][third_node]), (third_node, start, G[third_node][start])]
        cycle_weight = G[start][second_node] + G[second_node][third_node] + G[third_node][start]
        return cycle_weight, cycle

    # If G has at least 4 nodes and at most max_brute_force_n nodes, then all possible Hamiltonian cycles are computed
    # and one with the least total edge weight is selected.
    if 4 <= n <= max_brute_force_n:
        return tsp_brute_force(G, start)

    # If G has more than max_brute_force_n nodes then 2 Hamiltonian cycles are computed - one using the greedy approach
    # and one using Christofides algorithm. The one with the lesser total edge weight is selected. (If there is a tie,
    # then the cycle generated using the greedy approach is selected.)
    if n > max_brute_force_n:

        cycle_greedy_with_weight = tsp_greedy(G, start)
        cycle_greedy_weight = cycle_greedy_with_weight[0]

        cycle_christofides_with_weight = tsp_christofides(G, start)
        cycle_christofides_weight = cycle_christofides_with_weight[0]

        if cycle_greedy_weight <= cycle_christofides_weight:
            return cycle_greedy_with_weight

        if cycle_christofides_weight < cycle_greedy_weight:
            return cycle_christofides_with_weight


### EXAMPLES OF FUNCTION CALLS ON tsp(G, start, max_brute_force_n)


# G has 2 nodes, so there is only one possible Hamiltonian cycle. This cycle is hard-coded without involvement of algorithms.
# G = {
#     'A': {'A': 0, 'B': 12},
#     'B': {'A': 12, 'B': 0}
# }
# start = 'A'
# print(tsp(G, start))       # Prints (24, [('A', 'B', 12), ('B', 'A', 12)])
#
#
# # G has 3 nodes, so there are only two possible Hamiltonian cycles. They are essentially the same, just in reverse order
# # relative to each other. One of them is hard-coded without involvement of algorithms.
# G = {
#     'A': {'A': 0, 'B': 12, 'C': 3},
#     'B': {'A': 12, 'B': 0, 'C': 4},
#     'C': {'A': 3, 'B': 4, 'C': 0}
# }
# start = 'A'
# print(tsp(G, start))       # Prints (19, [('A', 'B', 12), ('B', 'C', 4), ('C', 'A', 3)])
#
#
# # G has 5 nodes, which is greater than 3 and less than the default value of 11 for max_brute_force_n.
# # Therefore, the Hamiltonian cycle is generated using the brute force approach.
# G = {
#     'A': {'A': 0, 'B': 12, 'C': 3, 'D': 6, 'E': 8},
#     'B': {'A': 12, 'B': 0, 'C': 4, 'D': 4, 'E': 5},
#     'C': {'A': 3, 'B': 4, 'C': 0, 'D': 9, 'E': 1},
#     'D': {'A': 6, 'B': 4, 'C': 9, 'D': 0, 'E': 4},
#     'E': {'A': 8, 'B': 5, 'C': 1, 'D': 4, 'E': 0}
# }
# start = 'A'
# print(tsp(G, start))       # Prints (19, [('A', 'C', 3), ('C', 'E', 1), ('E', 'B', 5), ('B', 'D', 4), ('D', 'A', 6)])
#
#
# # G has 12 nodes, which is greater than the default value of 11 for max_brute_force_n. If a value for max_brute_force_n
# # is not explicitly specified as an input in tsp(), then 2 Hamiltonian cycles are generated - one using the greedy approach
# # and one using Christofides algorithm - and the cycle with the lesser total edge weight is selected.
# # If we prefer to use the brute force approach then we can set max_brute_force_n to any integer 12 or larger.
# G = {
#     'A': {'A': 0, 'B': 37, 'C': 85, 'D': 64, 'E': 81, 'F': 20, 'G': 63, 'H': 97, 'I': 20, 'J': 58, 'K': 91, 'L': 28},
#     'B': {'A': 37, 'B': 0, 'C': 97, 'D': 44, 'E': 17, 'F': 14, 'G': 58, 'H': 72, 'I': 54, 'J': 67, 'K': 75, 'L': 16},
#     'C': {'A': 85, 'B': 97, 'C': 0, 'D': 28, 'E': 40, 'F': 39, 'G': 51, 'H': 79, 'I': 44, 'J': 60, 'K': 11, 'L': 14},
#     'D': {'A': 64, 'B': 44, 'C': 28, 'D': 0, 'E': 39, 'F': 7, 'G': 84, 'H': 67, 'I': 8, 'J': 66, 'K': 95, 'L': 72},
#     'E': {'A': 81, 'B': 17, 'C': 40, 'D': 39, 'E': 0, 'F': 29, 'G': 44, 'H': 23, 'I': 4, 'J': 79, 'K': 71, 'L': 47},
#     'F': {'A': 20, 'B': 14, 'C': 39, 'D': 7, 'E': 29, 'F': 0, 'G': 23, 'H': 75, 'I': 65, 'J': 97, 'K': 54, 'L': 58},
#     'G': {'A': 63, 'B': 58, 'C': 51, 'D': 84, 'E': 44, 'F': 23, 'G': 0, 'H': 97, 'I': 12, 'J': 70, 'K': 96, 'L': 99},
#     'H': {'A': 97, 'B': 72, 'C': 79, 'D': 67, 'E': 23, 'F': 75, 'G': 97, 'H': 0, 'I': 25, 'J': 65, 'K': 18, 'L': 93},
#     'I': {'A': 20, 'B': 54, 'C': 44, 'D': 8, 'E': 4, 'F': 65, 'G': 12, 'H': 25, 'I': 0, 'J': 88, 'K': 56, 'L': 26},
#     'J': {'A': 58, 'B': 67, 'C': 60, 'D': 66, 'E': 79, 'F': 97, 'G': 70, 'H': 65, 'I': 88, 'J': 0, 'K': 89, 'L': 42},
#     'K': {'A': 91, 'B': 75, 'C': 11, 'D': 95, 'E': 71, 'F': 54, 'G': 96, 'H': 18, 'I': 56, 'J': 89, 'K': 0, 'L': 41},
#     'L': {'A': 28, 'B': 16, 'C': 14, 'D': 72, 'E': 47, 'F': 58, 'G': 99, 'H': 93, 'I': 26, 'J': 42, 'K': 41, 'L': 0}
# }
# start = 'A'
# print(tsp(G, start))                             # Prints (303, [('A', 'F', 20), ('F', 'D', 7), ('D', 'I', 8), ('I', 'G', 12), ('G', 'E', 44), ('E', 'H', 23), ('H', 'K', 18), ('K', 'C', 11), ('C', 'L', 14), ('L', 'J', 42), ('J', 'B', 67), ('B', 'A', 37)])
# print(tsp(G, start, max_brute_force_n=12))       # Prints (275, [('A', 'I', 20), ('I', 'G', 12), ('G', 'F', 23), ('F', 'D', 7), ('D', 'C', 28), ('C', 'K', 11), ('K', 'H', 18), ('H', 'E', 23), ('E', 'B', 17), ('B', 'L', 16), ('L', 'J', 42), ('J', 'A', 58)])