from TSP_Brute_Force import tsp_brute_force
from TSP_Greedy import tsp_greedy
from TSP_Christofides import tsp_christofides




# G = {
#     'A': {'A': 0, 'B': 2, 'C': 3, 'D': 9},
#     'B': {'A': 2, 'B': 0, 'C': 6, 'D': 5},
#     'C': {'A': 3, 'B': 6, 'C': 0, 'D': 4},
#     'D': {'A': 9, 'B': 5, 'C': 4, 'D': 0}
# }
# start = 'A'


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
        return tsp(brute_force(G,start))

    # If G has more than max_brute_force_n nodes then 2 Hamiltonian cycles are computed - one using the greedy approach
    # and one using Christofides algorithm. The one with the lesser total edge weight is selected. (If there is a tie,
    # then the cycle generated using the greedy is selected.)
    if n > max_brute_force_n:

        cycle_greedy_with_weight = tsp_greedy(G, start)
        cycle_greedy_weight = cycle_greedy_with_weight[0]

        cycle_christofides_with_weight = tsp_christofides(G, start)
        cycle_christofides_weight = cycle_christofides_with_weight[0]

        if cycle_greedy_weight <= cycle_christofides_weight:
            return cycle_greedy_with_weight

        if cycle_christofides_weight < cycle_greedy_weight:
            return cycle_christofides_with_weight







G2 = {
    'A': {'A': 0, 'B': 3},
    'B': {'A': 3, 'B': 0}
}
start = 'A'

G3 = {
    'A': {'A': 0, 'B': 2, 'C': 3},
    'B': {'A': 2, 'B': 0, 'C': 6},
    'C': {'A': 3, 'B': 6, 'C': 0}
}
start = 'A'

print(tsp(G2, start))
print(tsp(G3, start))

n = 7
if 4 <= n <= 11:
    print(2*n)