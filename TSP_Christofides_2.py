from collections import defaultdict
from heapq import heappop, heappush


def union(parent, rank, x, y):
  """
  This function is needed for the minimum_spanning_tree() function.
  """
  xroot = find(parent, x)
  yroot = find(parent, y)

  if rank[xroot] < rank[yroot]:
    parent[xroot] = yroot
  elif rank[xroot] > rank[yroot]:
    parent[yroot] = xroot
  else:
    parent[yroot] = xroot
    rank[xroot] += 1

def find(parent, i):
  """
  This function is needed for the minimum_spanning_tree() function.
  """
  if parent[i] == i:
    return i
  return find(parent, parent[i])

def kruskal(G):
    result = []
    nodes = set()
    i = 0
    e = 0

    # Extract all the edges from the graph
    edges = []
    for node, neighbors in G.items():
        for neighbor in neighbors:
            # Only add edges that satisfy the triangle inequality
            if G[node][neighbor] <= G[node][neighbor] + G[neighbor][node]:
                edges.append((node, neighbor))

    # Sort the edges in non-decreasing order of their weight
    edges = sorted(edges, key=lambda item: G[item[0]][item[1]])

    parent = {}
    rank = {}

    # Initialize the disjoint sets
    for node in G.keys():
        parent[node] = node
        rank[node] = 0

    while e < len(G) - 1:
        u, v = edges[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            e = e + 1
            result.append((u, v))
            nodes.add(u)
            nodes.add(v)
            union(parent, rank, x, y)

    return sorted(list(nodes)), result


def nodes_with_odd_degree(graph):
    # Initialize an empty dictionary to store the degree of each node
    degree = {}

    # Iterate through the list of nodes and initialize their degree to 0
    for node in graph[0]:
        degree[node] = 0

    # Iterate through the list of edges and update the degree of each node
    for edge in graph[1]:
        degree[edge[0]] += 1
        degree[edge[1]] += 1

    # Initialize an empty list to store the nodes with odd degree
    odd_degree_nodes = []

    # Iterate through the dictionary of degrees and add the nodes with odd degree to the list
    for node, node_degree in degree.items():
        if node_degree % 2 == 1:
            odd_degree_nodes.append(node)

    # Return the ordered list of nodes with odd degree
    return sorted(odd_degree_nodes)


def node_induced_subgraph(G, nodes):
    # Initialize an empty subgraph
    subgraph = {}

    # Iterate through the list of nodes and add the corresponding edges to the subgraph
    for node in nodes:
        subgraph[node] = {}
        for neighbor, weight in G[node].items():
            if neighbor in nodes and neighbor != node:
                subgraph[node][neighbor] = weight

    return subgraph






################ SAVE THESE TEST CASES FOR LATER ################
# # Test case 1: 4 nodes
# G1 = {
#     "A": {"A": 0, "B": 3, "C": 4, "D": 5},
#     "B": {"A": 3, "B": 0, "C": 6, "D": 7},
#     "C": {"A": 4, "B": 6, "C": 0, "D": 8},
#     "D": {"A": 5, "B": 7, "C": 8, "D": 0}
# }
# minimum_spanning_tree1 = kruskal(G1)
# print(minimum_spanning_tree1)  # Prints (['A', 'B', 'C', 'D'], [('A', 'B'), ('A', 'C'), ('A', 'D')])
# nodes1 = nodes_with_odd_degree(minimum_spanning_tree1)
# print(nodes1)  # Prints ['A', 'B', 'C', 'D']
# subgraph1 = node_induced_subgraph(G1, nodes1)
# print(subgraph1, '\n')
#
#
# # Test case 2: 5 nodes
# G2 = {
#     "A": {"A": 0, "B": 2, "C": 3, "D": 4, "E": 5},
#     "B": {"A": 2, "B": 0, "C": 4, "D": 5, "E": 6},
#     "C": {"A": 3, "B": 4, "C": 0, "D": 6, "E": 7},
#     "D": {"A": 4, "B": 5, "C": 6, "D": 0, "E": 8},
#     "E": {"A": 5, "B": 6, "C": 7, "D": 8, "E": 0}
# }
# minimum_spanning_tree2 = kruskal(G2)
# print(minimum_spanning_tree2)  # Prints (['A', 'B', 'C', 'D', 'E'], [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E')])
# nodes2 = nodes_with_odd_degree(minimum_spanning_tree2)
# print(nodes2)  # Prints ['B', 'C', 'D', 'E']
# subgraph2 = node_induced_subgraph(G2, nodes2)
# print(subgraph2, '\n')
#
# # Test case 3: 5 nodes
# G3 = {
#     "A": {"A": 0, "B": 2, "C": 6, "D": 3, "E": 5},
#     "B": {"A": 2, "B": 0, "C": 4, "D": 5, "E": 4},
#     "C": {"A": 6, "B": 4, "C": 0, "D": 4, "E": 6},
#     "D": {"A": 3, "B": 5, "C": 4, "D": 0, "E": 3},
#     "E": {"A": 5, "B": 4, "C": 6, "D": 3, "E": 0}
# }
# minimum_spanning_tree3 = kruskal(G3)
# print(minimum_spanning_tree3)  # Prints (['A', 'B', 'C', 'D', 'E'], [('A', 'B'), ('A', 'D'), ('D', 'E'), ('B', 'C')])
# nodes3 = nodes_with_odd_degree(minimum_spanning_tree3)
# print(nodes3)  # Prints ['C', 'E']
# subgraph3 = node_induced_subgraph(G3, nodes3)
# print(subgraph3, '\n')
#
#
# # Test case 4 (just for nodes_with_odd_degree()): 7 nodes
# minimum_spanning_tree4 = (['A', 'B', 'C', 'D', 'E', 'F', 'G'], [('C', 'B'), ('C', 'D'), ('C', 'E'), ('D', 'E'), ('D', 'F'), ('G', 'F'), ('A', 'F'), ('F', 'E'), ('C', 'D')])
# nodes4 = nodes_with_odd_degree(minimum_spanning_tree4)
# print(nodes_with_odd_degree(minimum_spanning_tree4))  # Prints ['A', 'B', 'E', 'G']
################ SAVE THESE TEST CASES FOR LATER ################




# Test case from Wikipedia:
G = {
    "A": {"A": 0, "B": 1, "C": 2, "D": 1, "E": 1},
    "B": {"A": 1, "B": 0, "C": 1, "D": 2, "E": 1},
    "C": {"A": 2, "B": 1, "C": 0, "D": 1, "E": 1},
    "D": {"A": 1, "B": 2, "C": 1, "D": 0, "E": 1},
    "E": {"A": 1, "B": 1, "C": 1, "D": 1, "E": 0}
}
minimum_spanning_tree = kruskal(G)
print(minimum_spanning_tree)
nodes = nodes_with_odd_degree(minimum_spanning_tree)
print(nodes)
subgraph = node_induced_subgraph(G, nodes)
print(subgraph, '\n')



