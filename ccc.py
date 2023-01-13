import pprint
from ATSP import atsp

# COMPUTE INITIAL G AND NEAREST GAS STATIONS FROM INITIAL INPUT ['A','B','C','D','E']

G = {
    'A': {'A': 0, 'B': 120, 'C': 30, 'D': 60, 'E': 80},
    'B': {'A': 120, 'B': 0, 'C': 40, 'D': 40, 'E': 50},
    'C': {'A': 30, 'B': 40, 'C': 0, 'D': 90, 'E': 10},
    'D': {'A': 60, 'B': 40, 'C': 90, 'D': 0, 'E': 40},
    'E': {'A': 80, 'B': 50, 'C': 10, 'D': 40, 'E': 0}
}
start = 'A'

nearest_gas_stations = {
    'A': ['gas_station_A', 2],
    'B': ['gas_station_B', 4],
    'C': ['gas_station_C', 3],
    'D': ['gas_station_D', 6],
    'E': ['gas_station_E', 8]
}

# INPUT TO THE GRAPH UPDATE FUNCTION
unvisited_nodes = ['B', 'C', 'E']

# def update_G_at_gas_station(unvisited_nodes):
#     """
#     Returns a new graph with start='gas_station' which can be input into atsp().
#     """
#     #gstun = gas_station_to_unvisited_nodes(unvisited_nodes)   ### STILL NEED TO MAKE THIS FUNCTION; in the meantime I will hard-code a specific gstun dictionary below
#     gstun = {
#         'gas_station': 0,
#         'B': 2,
#         'C': 4,
#         'E': 1
#     }
#     updated_G = {node_outer: {node_inner: G[node_outer][node_inner] for node_inner in unvisited_nodes} for node_outer in unvisited_nodes}
#     for node in updated_G:
#         updated_G[node]['gas_station'] = gstun[node]
#     updated_G['gas_station'] = gstun
#
#     return updated_G
#
# pprint.pprint(update_G_at_gas_station(unvisited_nodes))




# def find_longest_route_before_filling_gas(G, start):





# if current_node == 'gas_station':
#     # Don't include distance to its gas station





### FROM start NODE WE SHOULD BEGIN BY GOING TO THE FURTHEST POSSIBLE GAS STATION. THEN ONLY APPLY THE GRAPH UPDATE FUNCTION FROM GAS STATIONS.
max_distance = 123
atsp_path = atsp(G, start)[1]

route_to_furthest_gas_station = [start]
distance_along_atsp_path = 0
for edge in atsp_path:
    edge_length = edge[2]
    next_node = edge[1]
    # If there is enough gas to make it to the gas station of the next atsp node, then travel to the next atsp node.
    if distance_along_atsp_path + edge_length + nearest_gas_stations[next_node][1] <= max_distance:
        route_to_furthest_gas_station.append(next_node)
        distance_along_atsp_path += edge_length
    else:
        break
# Append the nearest gas station of the last atsp node that was reached.
ngs = route_to_furthest_gas_station[-1]
route_to_furthest_gas_station.append(nearest_gas_stations[ngs][0])


print(atsp_path)
print(route_to_furthest_gas_station)
print(distance_along_atsp_path)
pprint.pprint(nearest_gas_stations)




# print(route_to_furthest_gas_station)

# for i in range(len(atsp_path)):
#     next_node = atsp_path[i][1]
#     next_edge_length = atsp_path[i][2]
#
#
#
#
# for edge in atsp_path:
#     next_node = edge[1]
#     edge_length = edge[2]
#     if route_length + edge_length + nearest_gas_stations[next_node[1]] > max_distance:

