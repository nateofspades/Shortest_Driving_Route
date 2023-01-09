import networkx as nx
import networkx.algorithms.approximation as nx_app
from TSP_Christofides import tsp_christofides, convert_graph_to_networkx_form
from Create_Graph_Function import create_graph_n_nodes
import time








# G = create_graph_n_nodes(12)
# print(G)
# G = convert_graph_to_networkx_form(G)
# cycle = nx_app.christofides(G)
# print(cycle)




#
# total_edge_weight = 0
# edge_list = []
# n = len(cycle)
# for i in range(n-1):
#     first_node = cycle[i]
#     second_node = cycle[i+1]
#     edge_weight = G[first_node][second_node]['weight']
#     edge_list.append((first_node, second_node, edge_weight))
#     total_edge_weight += edge_weight
# print(total_edge_weight, edge_list)



def tsp_christofides_2(G, start):

    G = convert_graph_to_networkx_form(G)
    cycle = nx_app.christofides(G)

    # If the cycle doesn't start at the appropriate node, then modify the cycle so that it does.
    if cycle[0] != start:
        start_index = cycle.index(start)
        cycle = cycle[start_index:] + cycle[1:start_index] + [start]

    total_edge_weight = 0
    edge_list = []
    n = len(cycle)
    for i in range(n-1):
        first_node = cycle[i]
        second_node = cycle[i + 1]
        edge_weight = G[first_node][second_node]['weight']
        edge_list.append((first_node, second_node, edge_weight))
        total_edge_weight += edge_weight
    return total_edge_weight, edge_list

#

# G = create_graph_n_nodes(200)
# start = 'N1'
# # print(G)
# #
# #
#
#
#
#
# #
# # # My modified networkx function
# t1 = time.time()
# print('networkx:  ', tsp_christofides_2(G, start))
# t2 = time.time()
# print(t2-t1)
# #
# #
# # My original function
# t1 = time.time()
# print('mine:      ', tsp_christofides(G, start))
# t2 = time.time()
# print(t2-t1)
