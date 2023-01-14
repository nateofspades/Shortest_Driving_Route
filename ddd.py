import pprint

# Input is a list of coordinate pairs, e.g. [(37.77584, -95.44304), (37.77714, -95.44361), (37.7878, -95.43828)]
# We want to convert this list to a dictionary



pairs = ['A','C','E']
# G = {}
# for pair in pairs:
#     G[pair] = {pair: 0}
#     for pair in pairs:
#         G[pair] = {pair: 0}

# pair_1 = pairs[0]
# # print(pair_1)
# for pair in pairs:
#     if pair != pair_1:
#         print(pair)



distances_temp = {
    'A': {'A': 0, 'B': 12, 'C': 3, 'D': 6, 'E': 8},
    'B': {'A': 12, 'B': 0, 'C': 4, 'D': 4, 'E': 5},
    'C': {'A': 3, 'B': 4, 'C': 0, 'D': 9, 'E': 1},
    'D': {'A': 6, 'B': 4, 'C': 9, 'D': 0, 'E': 4},
    'E': {'A': 8, 'B': 5, 'C': 1, 'D': 4, 'E': 0}
}


distances_temp = {
    'A': {'A': 0, 'B': 12, 'C': 3},
    'B': {'A': 12, 'B': 0, 'C': 4},
    'C': {'A': 3, 'B': 4, 'C': 0}
}

# distances_temp = {
#     'A': {'A': 0, 'B': 4, 'C': 1, 'D': 3, 'E': 7, 'F': 5, 'G': 6},
#     'B': {'A': 4, 'B': 0, 'C': 6, 'D': 5, 'E': 3, 'F': 2, 'G': 7},
#     'C': {'A': 1, 'B': 6, 'C': 0, 'D': 4, 'E': 2, 'F': 7, 'G': 3},
#     'D': {'A': 3, 'B': 5, 'C': 4, 'D': 0, 'E': 6, 'F': 1, 'G': 2},
#     'E': {'A': 7, 'B': 3, 'C': 2, 'D': 6, 'E': 0, 'F': 4, 'G': 5},
#     'F': {'A': 5, 'B': 2, 'C': 7, 'D': 1, 'E': 4, 'F': 0, 'G': 6},
#     'G': {'A': 6, 'B': 7, 'C': 3, 'D': 2, 'E': 5, 'F': 6, 'G': 0}
# }


distances_temp = {
    '(37.77584, -95.44304)': {'(37.77584, -95.44304)': 0, '(37.77714, -95.44361)': 12, '(37.7878, -95.43828)': 3},
    '(37.77714, -95.44361)': {'(37.77584, -95.44304)': 12, '(37.77714, -95.44361)': 0, '(37.7878, -95.43828)': 4},
    '(37.7878, -95.43828)': {'(37.77584, -95.44304)': 3, '(37.77714, -95.44361)': 4, '(37.7878, -95.43828)': 0}
}


# [(37.77584, -95.44304), (37.77714, -95.44361), (37.7878, -95.43828)]





def create_G(nodes):
    """
    Nodes is a list, where each element corresponds to one node.
    """

    n = len(nodes)
    G = {}

    # Generate the diagonal of 0's.
    for i in range(n):
        node_i = nodes[i]
        G[node_i] = {node_i: 0}

    # Generate the entries of G above the diagonal using API.
    for i in range(n-1):
        node_i = nodes[i]
        node_i_edges = {}
        for j in range(i, n):
            node_j = nodes[j]
            node_i_edges[node_j] = distances_temp[node_i][node_j]   # the distance between node_i and node_j; use the api
        G[node_i] = node_i_edges

    # Generate the entries of G below the diagonal by symmetry with the entries above the diagonal.
    for i in range(1, n):
        node_i = nodes[i]
        for j in range(i):
            node_j = nodes[j]
            G[node_i][node_j] = G[node_j][node_i]

    return G

nodes = list(distances_temp.keys())
pprint.pprint(create_G(nodes))