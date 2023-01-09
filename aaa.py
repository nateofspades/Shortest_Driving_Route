import networkx as nx
import networkx.algorithms.approximation as nx_app
from TSP_Christofides import tsp_christofides, convert_graph_to_networkx_form
from Create_Graph_Function import create_graph_n_nodes
import time

G = create_graph_n_nodes(12)
start = 'N1'
t1 = time.time()
print('mine:', tsp_christofides(G, start))
t2 = time.time()
print(t2-t1)


t1 = time.time()
G = convert_graph_to_networkx_form(G)
print('networkx:  ', nx_app.christofides(G))
t2 = time.time()
print(t2-t1)




L1 = (2,3,5)
L2 = (10,20,30)
L3 = (100,200,300)
print(list(zip(L1, L2, L3)))

L1 = [2,4]
L2 = (3,)
print(list(zip(L1, L2)))




perm = ('A', 'B', 'C', 'D')
G = {
    'A': {'A': 0, 'B': 2, 'C': 3, 'D': 9},
    'B': {'A': 2, 'B': 0, 'C': 6, 'D': 5},
    'C': {'A': 3, 'B': 6, 'C': 0, 'D': 4},
    'D': {'A': 9, 'B': 5, 'C': 4, 'D': 0}
}
start = 'A'

# i = 0: 2
# i = 1: 6
# i = 2: 4

print(list(zip(('A','B','C','D'), ('B','C','D') + ('A',), [2, 6, 4] + [9])))
print(list(zip(perm, perm[1:] + (start,), [G[perm[i]][perm[i + 1]] for i in range(len(perm) - 1)] + [G[perm[-1]][start]])))

print([G[perm[i]][perm[i + 1]] for i in range(len(perm) - 1)])

#print(list(zip(perm, perm[1:] + (start,), [G[perm[i]][perm[i + 1]] for i in range(len(perm) - 1)] + [G[perm[-1]][start]])))