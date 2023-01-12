import pprint

G = {
    'A': {'A': 0, 'B': 12, 'C': 3, 'D': 6, 'E': 8},
    'B': {'A': 12, 'B': 0, 'C': 4, 'D': 4, 'E': 5},
    'C': {'A': 3, 'B': 4, 'C': 0, 'D': 9, 'E': 1},
    'D': {'A': 6, 'B': 4, 'C': 9, 'D': 0, 'E': 4},
    'E': {'A': 8, 'B': 5, 'C': 1, 'D': 4, 'E': 0}
}
unvisited_nodes = ['B', 'C', 'E']
new_dict = {node_outer: {node_inner: G[node_outer][node_inner] for node_inner in unvisited_nodes} for node_outer in unvisited_nodes}
pprint.pprint(new_dict)

# def update_G(G, unvisited_nodes, current_node):
#     if current_node in unvisited_nodes:
#         updated_G = {node_outer: {node_inner: G[node_outer][node_inner] for node_inner in unvisited_nodes} for node_outer in unvisited_nodes}
#
#     else:
#         updated_G = {node_outer: {node_inner: G[node_outer][node_inner] for node_inner in unvisited_nodes} for node_outer in unvisited_nodes}
#
#
#     return updated_G

# pprint.pprint(update_G(G, unvisited_nodes, 'gas station'))

if current_location_type != 'gas station':
    #