import math
import heapq

def Christofides(G):
  # Find the minimum spanning tree of the graph
  T = MinimumSpanningTree(G)

  # Find the set of nodes that have odd degree in the minimum spanning tree
  odd_vertices = []
  for v in T:
    if len(T[v]) % 2 == 1:
      odd_vertices.append(v)

  # Initialize an empty graph for the matching
  M = {}
  for v in odd_vertices:
    M[v] = {}

  # Find a minimum weight perfect matching in the odd degree nodes
  while odd_vertices:
    # Choose an arbitrary node from the set of odd degree nodes
    v = odd_vertices.pop()
    # Initialize the shortest path distance and predecessor for v
    dist = {v: 0}
    pred = {v: None}
    # Initialize the priority queue with v
    Q = [(0, v)]
    # Initialize an empty set for visited nodes
    visited = set()
    # While the priority queue is not empty:
    while Q:
      # Pop the top node from the queue
      u = heapq.heappop(Q)[1]
      # Add it to the visited set
      visited.add(u)
      # For each neighbor of u:
      for neighbor in G[u]:
        # If the neighbor has not been visited and does not have a matching:
        if neighbor not in visited and neighbor not in M:
          # Update the shortest path distance and predecessor for the neighbor
          dist[neighbor] = dist[u] + G[u][neighbor]
          pred[neighbor] = u
          # Push the neighbor to the queue
          heapq.heappush(Q, (dist[neighbor], neighbor))
    # If a minimum weight perfect matching is not found:
    if v not in pred:
      # Return an empty list (no Hamiltonian cycle exists)
      return []
    # Otherwise:
    # Starting from v, follow the predecessor chain back to the beginning
    # This forms an alternating path in the matching
    u = v
    while u in pred:
      v = pred[u]
      # Add the edge (v, u) to the matching
      M[v][u] = G[v][u]
      # Remove the edge (u, v) from the matching (if it exists)
      M[u].pop(v, None)
      u = v
  # Initialize an empty graph for the eulerian tour
  H = {}
  for v in T:
    H[v] = {}
  # For each node in the matching:
  for v in M:
    # For each neighbor in the matching:
    for u in M[v]:
      # Add the edge (v, u) to the eulerian tour
      H[v][u] = G[v][u]
  # Find an eulerian tour of the eulerian tour graph
  tour = EulerianTour(H)
  # Convert the eulerian tour

  return tour

def MinimumSpanningTree(G):
  # Initialize the minimum spanning tree
  T = {}
  for v in G:
    T[v] = {}
  # Initialize the priority queue with all the edges in the graph
  Q = []
  for v in G:
    for u in G[v]:
      Q.append((G[v][u], v, u))
  # Sort the edges by weight
  heapq.heapify(Q)
  # Initialize an empty set for visited nodes
  visited = set()
  # While the priority queue is not empty:
  while Q:
    # Pop the top edge from the queue
    weight, v, u = heapq.heappop(Q)
    # If v and u are not connected:
    if v not in visited or u not in visited:
      # Add the edge (v, u) to the minimum spanning tree
      T[v][u] = weight
      # Add v and u to the visited set
      visited.add(v)
      visited.add(u)
  return T









G = {
    "A": {"B": 1, "C": 2, "D": 1, "E": 1},
    "B": {"A": 1, "C": 1, "D": 2, "E": 1},
    "C": {"A": 2, "B": 1, "D": 1, "E": 1},
    "D": {"A": 1, "B": 2, "C": 1, "E": 1},
    "E": {"A": 1, "B": 1, "C": 1, "D": 1}
}
print(MinimumSpanningTree(G))
print(Christofides(G))







# T = {
#   'A': {'B': 2, 'C': 3},
#   'B': {'A': 2, 'C': 1, 'D': 3},
#   'C': {'A': 3, 'B': 1, 'D': 2},
#   'D': {'B': 3, 'C': 2}
# }
#
# T = MinimumSpanningTree(T)
# print(T)
#
#
#
# G = {
#     "A": {"B": 1, "C": 2, "D": 1, "E": 1},
#     "B": {"A": 1, "C": 1, "D": 2, "E": 1},
#     "C": {"A": 2, "B": 1, "D": 1, "E": 1},
#     "D": {"A": 1, "B": 2, "C": 1, "E": 1},
#     "E": {"A": 1, "B": 1, "C": 1, "D": 1}
# }
# print(MinimumSpanningTree(G))



