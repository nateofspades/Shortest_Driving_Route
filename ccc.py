import pprint

unvisited_nodes = ['B', 'C', 'E']

G = {
    'A': {'A': 0, 'B': 12, 'C': 3, 'D': 6, 'E': 8},
    'B': {'A': 12, 'B': 0, 'C': 4, 'D': 4, 'E': 5},
    'C': {'A': 3, 'B': 4, 'C': 0, 'D': 9, 'E': 1},
    'D': {'A': 6, 'B': 4, 'C': 9, 'D': 0, 'E': 4},
    'E': {'A': 8, 'B': 5, 'C': 1, 'D': 4, 'E': 0}
}

# G_new = G[unvisited_nodes]
# print(G_new)



# {j: k[j] for j in unvisited_nodes}



# new_dict = {node_outer: {node_inner: G[node_inner] for node_inner in unvisited_nodes} for node_outer in unvisited_nodes}
# pprint.pprint(new_dict)


# node_outer = 'B'
# print(G[node_outer])

# node_inner = 'B'
# pprint.pprint({node_inner: G[node_outer][node_inner] for node_inner in unvisited_nodes})



new_dict = {node_outer: G[node_outer] for node_outer in unvisited_nodes}
print(new_dict)

{node_outer: G[node_outer][node_inner] for node_inner in unvisited_nodes}


# original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# subset_keys = ['b', 'd']
# new_dict = {k: original_dict[k] for k in subset_keys if k in original_dict}
# print(new_dict)





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