import random

def create_random_G(nodes, max_weight):
  """
  This is a function made to generate random graph dictionaries for the purpose of testing the tsp and atsp functions.

  :param nodes (list): The list of nodes that the graph will use.

  :param max_weight (int): The maximum edge weight the graph can have. All edge weights are from 0.5*max_weight to max_weight.
    The purpose of this restriction is to ensure that the triangle inequality for the output will be respected.

  :return: A graph that can be input into any of the tsp functions.
  """

  # Initialize the dictionary with the nodes as keys and empty dictionaries as values
  weight_dict = {n: {} for n in nodes}

  # Iterate through the nodes and add the edge weights to the dictionary
  for i in range(len(nodes)):
    for j in range(i, len(nodes)):
      # Set the weight of the edge between a node and itself to 0
      if i == j:
        weight_dict[nodes[i]][nodes[j]] = 0
      # Set the weight of any other edge to a random integer weight that is at least half of the maximum weight and at most the maximum weight
      else:
        weight = random.randint(max_weight // 2, max_weight)
        weight_dict[nodes[i]][nodes[j]] = weight
        weight_dict[nodes[j]][nodes[i]] = weight

  return weight_dict