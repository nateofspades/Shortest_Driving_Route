import networkx as nx



# Step 1: Convert G to the appropriate format so that it can be used by the networkx library.
G = [("A", "B", 7), ("A", "C", 2), ("B", "C", 3), ("B", "D", 1), ("C", "E", 4), ("D", "E", 6)]
print(G)
G_temp = []
for edge in G:
    G_temp.append((edge[0], edge[1], {'weight': edge[2]}))
G = nx.Graph(G_temp)
print(G.edges(data=True), '\n')




# 2. Calculate minimum spanning tree T of G.
# G = nx.cycle_graph(4)
# G.add_edge(0, 3, weight=2)         # See H in step 5 for a more convenient way to create a graph that skips this step.
# T = nx.minimum_spanning_tree(G)
# print(G.edges(data=True))
# print(T.nodes, T.edges, '\n')
T = nx.minimum_spanning_tree(G)
print(T.edges(data=True))



# 3. Calculate the set of vertices O with odd degree in T
# G = nx.Graph()
# E2  = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "E"), ("D", "E")]
# G.add_edges_from(E2)
# print(G.nodes)
# print(G.edges)
# print(list(G.degree(['A', 'B', 'C', 'D', 'E'])))
print(list(T.degree))
T_nodes_and_degrees = T.degree
O = []
for node, degree in T_nodes_and_degrees:
    if degree%2 == 1:
        O.append(node)
print(O, '\n')




# 4. Form the subgraph S of G using only the vertices of O
# G = nx.Graph()
# E2  = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "E"), ("D", "E")]
# G.add_edges_from(E2)
# H = nx.induced_subgraph(G, ['A', 'B', 'E'])
# print(H.edges)
# print(H.nodes)

S = nx.induced_subgraph(G, O)
print(S.edges, '\n')


# 5. Construct a minimum-weight perfect matching M in this subgraph
### (In our case a minimum-weight maximal matching)
# G = nx.Graph()
# edges = [("A", "B", 6), ("A", "C", 2), ("B", "C", 1), ("B", "D", 7), ("C", "E", 9), ("D", "E", 3)]
# G.add_weighted_edges_from(edges)
# print(sorted(nx.min_weight_matching(G)), '\n')  # Prints [('C', 'B'), ('D', 'E')]
M = nx.min_weight_matching(S)
M = nx.Graph(M)  # Convert from a set object to a graph object
print(M.edges, '\n')


# 6. Unite matching and spanning tree T ∪ M to form an Eulerian multigraph H; unions the edge sets and vertex sets
# G = nx.MultiGraph([("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "E"), ("D", "E")])
# H = nx.MultiGraph([('A', 'C'), ('F', 'G')])
# R = nx.MultiGraph(nx.compose(G, H))
# print(R.nodes)
# print(R.edges)



H = nx.MultiGraph(list(T.edges) + list(M.edges))
print(H.edges)




# 7. Calculate Euler tour in H
# G = nx.Graph([("E", "D"), ("C", "B"), ("A", "B"), ("D", "A"), ("A", "C"), ("E", "A")])
# print(list(nx.eulerian_circuit(G, source="A")))  # source is the starting node


print(list(nx.eulerian_circuit(H, source="A")))
print(list(nx.eulerian_circuit(H, source="B")))



# 8. Remove repeated vertices, giving the algorithm's output.
#def remove_repeated_vertices(euler_tour):


# euler_tour = [('A', 'B'), ('B', 'C'), ('C', 'A'), ('A', 'D'), ('D', 'E'), ('E', 'A')]
#
# hamiltonian_cycle = []
# hamiltonian_cycle.append(euler_tour[0][0])
# hamiltonian_cycle.append(euler_tour[0][1])
# for edge in euler_tour[1:]:
#     if edge[1] not in hamiltonian_cycle:
#         hamiltonian_cycle.append(edge[1])
#
# # The hamiltonian cycle should end with the same vertex it started with
# hamiltonian_cycle.append(euler_tour[0][0])
#
# print(hamiltonian_cycle)








