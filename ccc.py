import pprint

nearest_gas_stations = {
    'A': ['gas_A', 2],
    'B': ['gas_B', 4],
    'C': ['gas_C', 3],
    'D': ['gas_D', 6],
    'E': ['gas_E', 8]
}
print(nearest_gas_stations)

G = {
    'A': {'A': 0, 'B': 120, 'C': 30, 'D': 60, 'E': 80},
    'B': {'A': 120, 'B': 0, 'C': 4, 'D': 4, 'E': 50},
    'C': {'A': 30, 'B': 40, 'C': 0, 'D': 90, 'E': 10},
    'D': {'A': 60, 'B': 40, 'C': 90, 'D': 0, 'E': 40},
    'E': {'A': 80, 'B': 50, 'C': 10, 'D': 40, 'E': 0}
}
unvisited_nodes = ['B', 'C', 'E']
# new_dict = {node_outer: {node_inner: G[node_outer][node_inner] for node_inner in unvisited_nodes} for node_outer in unvisited_nodes}
# pprint.pprint(new_dict)

# def update_G(G, unvisited_nodes, gas_station):
#
#     updated_G = {node_outer: {node_inner: G[node_outer][node_inner] for node_inner in unvisited_nodes} for node_outer in unvisited_nodes}
#     for node in updated_G
#     else:
#         updated_G = {node_outer: {node_inner: G[node_outer][node_inner] for node_inner in unvisited_nodes} for node_outer in unvisited_nodes}
#
#
#     return updated_G

### Already been to 'A' and D'; updating G at 'gas_D'
# Compute distance from current 'gas_station' to remaining nodes B, C and E   - will need a function for this
gas_station = {
    'gas_station': 0,
    'B': 2,
    'C': 4,
    'E': 1
}

updated_G = {node_outer: {node_inner: G[node_outer][node_inner] for node_inner in unvisited_nodes} for node_outer in unvisited_nodes}
for node in updated_G:
    updated_G[node]['gas_station'] = gas_station[node]

updated_G['gas_station'] = gas_station


pprint.pprint(updated_G)

# for node in updated_G:
#     ngs = nearest_gas_stations[node]
#     edges = updated_G[node]
#     edges[neares]
#     node[nearest_gas_stations[]]

