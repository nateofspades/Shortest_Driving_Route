from typing import Dict, List
import math

from typing import Dict, List
import math

def Christofides(destinations: List[str], distances: Dict[str, Dict[str, float]], start: str) -> Dict[str, Dict[str, float]]:
  mst = minimum_spanning_tree(distances)
  graph = add_eulerian_path(mst, start, distances)
  graph = add_perfect_matching(graph, distances)
  return graph

def minimum_spanning_tree(graph: Dict[str, Dict[str, float]]) -> Dict[str, Dict[str, float]]:
  # Implement Kruskal's algorithm to find the minimum spanning tree of the graph
  mst = {v: v for v in graph}
  edges = []
  for u in graph:
    for v in graph[u]:
      edges.append((graph[u][v], u, v))
  edges.sort()
  for w, u, v in edges:
    if find(u, mst) != find(v, mst):
      union(u, v, mst)
  result = {}
  for u, v in mst.items():
    if u not in result:
      result[u] = {}
    result[u][v] = graph[u][v]
  return result

def find(u, parent):
  if parent[u] != u:
    parent[u] = find(parent[u], parent)
  return parent[u]

def union(u, v, parent):
  u = find(u, parent)
  v = find(v, parent)
  parent[v] = u

def add_eulerian_path(graph: Dict[str, Dict[str, float]], start: str, distances: Dict[str, Dict[str, float]]) -> Dict[str, Dict[str, float]]:
  current_vertex = start
  stack = [current_vertex]
  while len(stack) > 0:
    next_vertex = None
    if graph[current_vertex]:
      next_vertex = min(graph[current_vertex], key=lambda x: distances[current_vertex][x])
    if next_vertex:
      graph[current_vertex][next_vertex] = distances[current_vertex][next_vertex]
      graph[next_vertex][current_vertex] = distances[next_vertex][current_vertex]
      del graph[current_vertex][next_vertex]
      if next_vertex in graph:
        if current_vertex in graph[next_vertex]:
          del graph[next_vertex][current_vertex]
      current_vertex = next_vertex
      stack.append(current_vertex)
    else:
      stack.pop()
  return graph


def add_perfect_matching(graph: Dict[str, Dict[str, float]], distances: Dict[str, Dict[str, float]]) -> Dict[str, Dict[str, float]]:
  # Implement the algorithm to find a perfect matching in the graph
  # First, find the odd-degree vertices in the graph
  odd_vertices = [v for v in graph if len(graph[v]) % 2 == 1]
  # While there are more than 0 odd-degree vertices:
  while len(odd_vertices) > 0:
    # Select an arbitrary odd-degree vertex v
    v = odd_vertices[0]
    # Select an arbitrary vertex u that is not connected to v
    u = [x for x in graph if x not in graph[v]][0]
    # Add the edge (u, v) to the graph with weight equal to the distance between u and v
    graph[u][v] = distances[u][v]
    graph[v][u] = distances[v][u]
    # Recompute the list of odd-degree vertices
    odd_vertices = [v for v in graph if len(graph[v]) % 2 == 1]
  return graph


distances = {
  'A': {'A': 0, 'B': 10, 'C': 20, 'D': 30},
  'B': {'A': 10, 'B': 0, 'C': 15, 'D': 25},
  'C': {'A': 20, 'B': 15, 'C': 0, 'D': 40},
  'D': {'A': 30, 'B': 25, 'C': 40, 'D': 0}
}

print(Christofides(['A','B','C','D'], distances, 'A'))