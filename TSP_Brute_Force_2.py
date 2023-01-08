from itertools import permutations

def traveling_salesman(G, start):
  # G is a list of tuples representing the edges of the complete graph
  # start is the node where the Hamiltonian cycle will begin and end

  # create a list of all the nodes in the graph
  nodes = [node for edge in G for node in edge[:2]]
  # remove any duplicate nodes
  nodes = list(set(nodes))

  # create a list of all possible permutations of the nodes
  node_permutations = permutations(nodes)

  # initialize the minimum weight and corresponding permutation
  min_weight = float("inf")
  min_permutation = None

  # iterate over each permutation of the nodes
  for permutation in node_permutations:
    # check if the permutation starts with the starting node
    if permutation[0] != start:
      continue

    # create a list to store the edges in the permutation
    edges = []

    # iterate over pairs of nodes in the permutation
    for i in range(len(permutation) - 1):
      # get the weight of the edge between the current and next node
      weight = next((edge[2] for edge in G if (edge[0] == permutation[i] and edge[1] == permutation[i+1]) or (edge[1] == permutation[i] and edge[0] == permutation[i+1])), float("inf"))
      # add the edge to the list of edges
      edges.append((permutation[i], permutation[i+1], weight))

    # get the weight of the edge between the last and first node in the permutation
    weight = next((edge[2] for edge in G if (edge[0] == permutation[-1] and edge[1] == start) or (edge[1] == permutation[-1] and edge[0] == start)), float("inf"))
    # add the edge to the list of edges
    edges.append((permutation[-1], start, weight))

    # calculate the total weight of the edges in the permutation
    total_weight = sum(edge[2] for edge in edges)

    # if the total weight is less than the current minimum weight, update the minimum weight and permutation
    if total_weight < min_weight:
      min_weight = total_weight
      min_permutation = edges

  # return the minimum weight and corresponding permutation of edges
  return (min_weight, min_permutation)


# Test case 1: 4 nodes
G = [("A", "B", 2), ("A", "C", 3), ("A", "D", 9),
     ("B", "C", 6), ("B", "D", 5),
     ("C", "D", 4)]
print(traveling_salesman(G, "A"))    # Should print something equivalent to (14, ['A', 'B', 'D', 'C', 'A'])


# Test case 2: 4 nodes
G = [("A", "B", 8), ("A", "C", 6), ("A", "D", 3),
     ("B", "C", 5), ("B", "D", 5),
     ("C", "D", 1)]
print(traveling_salesman(G, "A"))    # Should print something equivalent to (17, ['A', 'B', 'C', 'D', 'A'])

# Test case 3: 5 nodes
G = [("A", "B", 12), ("A", "C", 3), ("A", "D", 6), ("A", "D", 8),
     ("B", "C", 4), ("B", "D", 4), ("B", "E", 5),
     ("C", "D", 9), ("C", "E", 1),
     ("D", "E", 4)]
print(traveling_salesman(G, "A"))     # Should print something equivalent to (19, ['A', 'C', 'E', 'B', 'D', 'A'])


# Test case 4: 10 nodes
G =  [("A", "B", 12), ("A", "C", 3), ("A", "D", 6), ("A", "E", 8), ("A", "F", 7), ("A", "G", 9), ("A", "H", 1), ("A", "I", 13), ("A", "J", 8),
      ("B", "C", 2), ("B", "D", 2), ("B", "E", 9), ("B", "F", 14), ("B", "G", 17), ("B", "H", 6), ("B", "I", 3), ("B", "J", 4),
      ("C", "D", 1), ("C", "E", 5), ("C", "F", 5), ("C", "G", 2), ("C", "H", 4), ("C", "I", 3), ("C", "J", 7),
      ("D", "E", 3), ("D", "F", 3), ("D", "G", 10), ("D", "H", 19), ("D", "I", 20), ("D", "J", 28),
      ("E", "F", 4), ("E", "G", 11), ("E", "H", 14), ("E", "I", 8), ("E", "J", 1),
      ("F", "G", 12), ("F", "H", 1), ("F", "I", 1), ("F", "J", 2),
      ("G", "H", 13), ("G", "I", 16), ("G", "J", 18),
      ("H", "I", 6), ("H", "J", 8),
      ("I", "J", 2)]

import time
t1 = time.time()
print(traveling_salesman(G, "A"))     # Should print something equivalent to (24, ['A', 'G', 'C', 'B', 'D', 'E', 'J', 'I', 'F', 'H', 'A'])
t2 = time.time()
print(t2-t1)