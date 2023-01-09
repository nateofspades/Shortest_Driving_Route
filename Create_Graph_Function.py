import random

def create_graph_n_nodes(n):
    """
    This function creates a random graph G of n nodes so that we can test how long each of the tsp functions take to run for various graph sizes.
    :param n: A positive integer representing the number of nodes in G.
    :return: A graph G with n nodes, 'N1', 'N2', ..., 'Nn'.
    """
    edge_weights = {}
    for i in range(1, n+1):
        node1 = 'N' + str(i)
        edge_weights[node1] = {}
        for j in range(1, n+1):
            node2 = 'N' + str(j)
            if i == j:
                edge_weights[node1][node2] = 0
            else:
                if node1 in edge_weights and node2 in edge_weights[node1]:
                    edge_weights[node1][node2] = edge_weights[node1][node2]
                else:
                    edge_weights[node1][node2] = random.randint(1, n)
                    if node2 in edge_weights:
                        edge_weights[node2][node1] = edge_weights[node1][node2]
                    else:
                        edge_weights[node2] = {}
                        edge_weights[node2][node1] = edge_weights[node1][node2]
    return edge_weights
