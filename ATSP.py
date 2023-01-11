from ATSP_Brute_Force import atsp_brute_force
from ATSP_Greedy import atsp_greedy
from ATSP_Christofides import atsp_christofides

def atsp(G, start, max_brute_force_n = 11):

    nodes = list(G.keys())
    n = len(nodes)
    nodes.remove(start)

    # If G has 2 nodes then there is just one possible path, which is hardcoded below.
    if n == 2:
        second_node = nodes[0]
        path = [(start, second_node, G[start][second_node])]
        path_weight = G[start][second_node]
        return path_weight, path

    # If G has at least 3 nodes and at most max_brute_force_n nodes, then all possible paths are computed
    # and one with the least total edge weight is selected.
    if 3 <= n <= max_brute_force_n:
        return atsp_brute_force(G, start)

    # If G has more than max_brute_force_n nodes then 2 paths are computed - one using the greedy approach
    # and one using Christofides algorithm. The one with the lesser total edge weight is selected. (If there is a tie,
    # then the path generated using the greedy approach is selected.)
    if n > max_brute_force_n:

        path_greedy_with_weight = atsp_greedy(G, start)
        path_greedy_weight = path_greedy_with_weight[0]

        path_christofides_with_weight = atsp_christofides(G, start)
        path_christofides_weight = path_christofides_with_weight[0]

        if path_greedy_weight <= path_christofides_weight:
            return path_greedy_with_weight

        if path_christofides_weight < path_greedy_weight:
            return path_christofides_with_weight


### EXAMPLES OF FUNCTION CALLS ON atsp(G, start, max_brute_force_n)


# G has 2 nodes, so there is only one possible path. This path is hard-coded without involvement of algorithms.
G = {
    'A': {'A': 0, 'B': 12},
    'B': {'A': 12, 'B': 0}
}
start = 'A'
print(atsp(G, start))       # Prints (12, [('A', 'B', 12)])


# G has 3 nodes, so the path is generated using the brute force approach.
G = {
    'A': {'A': 0, 'B': 12, 'C': 3},
    'B': {'A': 12, 'B': 0, 'C': 4},
    'C': {'A': 3, 'B': 4, 'C': 0}
}
start = 'A'
print(atsp(G, start))       # Prints (7, [('A', 'C', 3), ('C', 'B', 4)])


# G has 5 nodes, which is greater than 3 and less than the default value of 11 for max_brute_force_n.
# Therefore, the path is generated using the brute force approach.
G = {
    'A': {'A': 0, 'B': 12, 'C': 3, 'D': 6, 'E': 8},
    'B': {'A': 12, 'B': 0, 'C': 4, 'D': 4, 'E': 5},
    'C': {'A': 3, 'B': 4, 'C': 0, 'D': 9, 'E': 1},
    'D': {'A': 6, 'B': 4, 'C': 9, 'D': 0, 'E': 4},
    'E': {'A': 8, 'B': 5, 'C': 1, 'D': 4, 'E': 0}
}
start = 'A'
print(atsp(G, start))       # Prints (12, [('A', 'C', 3), ('C', 'E', 1), ('E', 'D', 4), ('D', 'B', 4)])


# G has 12 nodes, which is greater than the default value of 11 for max_brute_force_n. If a value for max_brute_force_n
# is not explicitly specified as an input in atsp(), then 2 paths are generated - one using the greedy approach
# and one using Christofides algorithm - and the path with the lesser total edge weight is selected.
# If we prefer to use the brute force approach then we can set max_brute_force_n to any integer 12 or larger.
G = {
    'A': {'A': 0, 'B': 37, 'C': 85, 'D': 64, 'E': 81, 'F': 20, 'G': 63, 'H': 97, 'I': 20, 'J': 58, 'K': 91, 'L': 28},
    'B': {'A': 37, 'B': 0, 'C': 97, 'D': 44, 'E': 17, 'F': 14, 'G': 58, 'H': 72, 'I': 54, 'J': 67, 'K': 75, 'L': 16},
    'C': {'A': 85, 'B': 97, 'C': 0, 'D': 28, 'E': 40, 'F': 39, 'G': 51, 'H': 79, 'I': 44, 'J': 60, 'K': 11, 'L': 14},
    'D': {'A': 64, 'B': 44, 'C': 28, 'D': 0, 'E': 39, 'F': 7, 'G': 84, 'H': 67, 'I': 8, 'J': 66, 'K': 95, 'L': 72},
    'E': {'A': 81, 'B': 17, 'C': 40, 'D': 39, 'E': 0, 'F': 29, 'G': 44, 'H': 23, 'I': 4, 'J': 79, 'K': 71, 'L': 47},
    'F': {'A': 20, 'B': 14, 'C': 39, 'D': 7, 'E': 29, 'F': 0, 'G': 23, 'H': 75, 'I': 65, 'J': 97, 'K': 54, 'L': 58},
    'G': {'A': 63, 'B': 58, 'C': 51, 'D': 84, 'E': 44, 'F': 23, 'G': 0, 'H': 97, 'I': 12, 'J': 70, 'K': 96, 'L': 99},
    'H': {'A': 97, 'B': 72, 'C': 79, 'D': 67, 'E': 23, 'F': 75, 'G': 97, 'H': 0, 'I': 25, 'J': 65, 'K': 18, 'L': 93},
    'I': {'A': 20, 'B': 54, 'C': 44, 'D': 8, 'E': 4, 'F': 65, 'G': 12, 'H': 25, 'I': 0, 'J': 88, 'K': 56, 'L': 26},
    'J': {'A': 58, 'B': 67, 'C': 60, 'D': 66, 'E': 79, 'F': 97, 'G': 70, 'H': 65, 'I': 88, 'J': 0, 'K': 89, 'L': 42},
    'K': {'A': 91, 'B': 75, 'C': 11, 'D': 95, 'E': 71, 'F': 54, 'G': 96, 'H': 18, 'I': 56, 'J': 89, 'K': 0, 'L': 41},
    'L': {'A': 28, 'B': 16, 'C': 14, 'D': 72, 'E': 47, 'F': 58, 'G': 99, 'H': 93, 'I': 26, 'J': 42, 'K': 41, 'L': 0}
}
start = 'A'
print(atsp(G, start))                             # Prints (250, [('A', 'F', 20), ('F', 'D', 7), ('D', 'I', 8), ('I', 'E', 4), ('E', 'B', 17), ('B', 'L', 16), ('L', 'C', 14), ('C', 'K', 11), ('K', 'H', 18), ('H', 'J', 65), ('J', 'G', 70)])
print(atsp(G, start, max_brute_force_n=12))       # Prints (217, [('A', 'I', 20), ('I', 'G', 12), ('G', 'F', 23), ('F', 'D', 7), ('D', 'C', 28), ('C', 'K', 11), ('K', 'H', 18), ('H', 'E', 23), ('E', 'B', 17), ('B', 'L', 16), ('L', 'J', 42)])