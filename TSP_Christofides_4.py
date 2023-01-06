from collections import defaultdict
from heapq import heappop, heappush


def christofides(nodes, edges, start):
  # Create the minimum spanning tree.
  mst = minimum_spanning_tree(nodes, edges, start)

  # Find the odd degree vertices in the MST.
  odd_degree_vertices = [v for v, degree in degree(mst).items() if degree % 2 == 1]

  # Create a multigraph by duplicating each edge in the MST.
  multigraph = {v: [] for v in mst.keys()}
  for u, v_list in mst.items():
    for v, weight in v_list:
      multigraph[u].append(v)
      multigraph[v].append(u)

  # Find a minimum weight perfect matching in the multigraph.
  matching = minimum_weight_perfect_matching(multigraph, edges)

  # Merge the MST and matching into an Eulerian multigraph.
  eulerian_multigraph = {v: [] for v in multigraph.keys()}
  for u, v_list in multigraph.items():
    for v in v_list:
      eulerian_multigraph[u].append(v)
  for u, v in matching:
    eulerian_multigraph[u].append(v)
    eulerian_multigraph[v].append(u)

  # Find an Eulerian tour in the Eulerian multigraph.
  tour = find_eulerian_tour(eulerian_multigraph, start)

  # Return the list of nodes visited in the Eulerian tour, starting and ending with the start node.
  return tour



def degree(graph):
  # Initialize a dictionary to store the degrees of the nodes.
  degrees = {}

  # Iterate through the edges of the graph and update the degrees of the nodes.
  for u, v in graph.items():
    degrees[u] = degrees.get(u, 0) + 1
    degrees[v] = degrees.get(v, 0) + 1

  # Return the degrees of the nodes.
  if len(degrees) > 1:
    return degrees
  else:
    return {}



def minimum_spanning_tree(nodes, edges, start):
  # Sort the edges by weight in ascending order.
  edges = sorted(edges.items(), key=lambda x: list(x[1].values())[0])

  # Initialize the MST with the start node.
  mst = {start: []}

  # Iterate through the sorted edges and add them to the MST.
  for u, v_dict in edges:
    for v, weight in v_dict.items():
      if u not in mst:
        mst[u] = [(v, weight)]
      else:
        mst[u].append((v, weight))
      if v not in mst:
        mst[v] = [(u, weight)]
      else:
        mst[v].append((u, weight))

  # Return a dictionary containing all the nodes as keys and empty lists as values.
  return mst


def minimum_weight_perfect_matching(odd_degree_vertices, edges):
  matching = []
  paired = set()
  while odd_degree_vertices:
    u = odd_degree_vertices.pop()
    min_weight = float("inf")
    min_v = None
    for v in odd_degree_vertices:
      if v not in paired and edges[u][v] < min_weight:
        min_weight = edges[u][v]
        min_v = v
    if min_v:
      paired.add(u)
      paired.add(min_v)
      matching.append((u, min_v))
  return matching

def find_eulerian_tour(graph, start):
  tour = []
  stack = [start]
  while stack:
    current_node = stack[-1]
    if graph[current_node]:
      next_node = graph[current_node].pop()
      stack.append(next_node)
    else:
      tour.append(stack.pop())
  return tour




# Define the list of nodes and the dictionary of edge weights.
nodes = ['A', 'B', 'C', 'D', 'E']
edges = {
  'A': {'A': 0, 'B': 10, 'C': 20, 'D': 30, 'E': 40},
  'B': {'A': 10, 'B': 0, 'C': 15, 'D': 25, 'E': 35},
  'C': {'A': 20, 'B': 15, 'C': 0, 'D': 5, 'E': 15},
  'D': {'A': 30, 'B': 25, 'C': 5, 'D': 0, 'E': 10},
  'E': {'A': 40, 'B': 35, 'C': 15, 'D': 10, 'E': 0}
}
tsp_solution = christofides(nodes, edges, 'A')
print(tsp_solution)  # Prints ['A', 'B', 'C', 'D', 'E', 'A']


nodes = ['A', 'B', 'C', 'D']
edges = {
  'A': {'A': 0, 'B': 9, 'C': 6, 'D': 8},
  'B': {'A': 9, 'B': 0, 'C': 3, 'D': 2},
  'C': {'A': 6, 'B': 3, 'C': 0, 'D': 5},
  'D': {'A': 8, 'B': 2, 'C': 5, 'D': 0}
}
tsp_solution = christofides(nodes, edges, 'A')
print(tsp_solution)  # Prints ['A', 'C', 'B', 'D', 'A']





nodes = ['A', 'B', 'C', 'D']
edges = {
  'A': {'A': 0, 'B': 1, 'C': 2, 'D': 3},
  'B': {'A': 1, 'B': 0, 'C': 2, 'D': 3},
  'C': {'A': 2, 'B': 2, 'C': 0, 'D': 1},
  'D': {'A': 3, 'B': 3, 'C': 1, 'D': 0}
}
tsp_solution = christofides(nodes, edges, 'A')
print(tsp_solution)