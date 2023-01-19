# Shortest_Driving_Route

Suppose you are a trucker who needs to make deliveries in multiple locations. Two questions you might naturally ask yourself are:

1. "What is the shortest route I can take?"
2. "At which point(s) along the route should I begin to look for a gas station?"

The focus of this project is to answer both of these questions. 

Screenshots of two examples of the end result of this project can be seen at the links below:

[Mapbox_Example_ATSP_Screenshots](https://github.com/nateofspades/Shortest_Driving_Route/tree/master/Mapbox/Mapbox_Example_ATSP_Screenshots): This consists of 4 screenshots of a route that begins in Quebec City and makes a delivery in each of Montreal, Ottawa, Kingston and London - where the route ends. Each of these locations are labeled in **blue**. The map also labels 2 suggested locations for when the driver should begin to look for a gas station in **red**. 

[Mapbox_Example_TSP_Screenshots](https://github.com/nateofspades/Shortest_Driving_Route/tree/master/Mapbox/Mapbox_Example_TSP_Screenshots). This is another set of 4 screenshots of a route that begins in Quebec City and makes a delivery in each of Montreal, Ottawa, Kingston and London. In this route the trucker must return to the starting point, Quebec city, after visiting the last delivery point in London.

This project is a direct application of the **Traveling Salesman Problem** using the **Mapbox Directions API**. Here's what I did:

Step 1: Write Python scripts that compute a cycle of a weighted complete graph G which starts at a given node and passes through all of the nodes of G. A cycle of G which passes through all nodes of G is called a **Hamiltonian cycle**. There are 3 such scripts, each corresponding to a different way that a Hamiltonian cycle can be computed: </br>
[TSP_Brute_Force.py](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/TSP_Brute_Force.py): This computes all of the possible Hamiltonian cycles of G starting at a given node and selects one with the minimum total edge weight.
[TSP_Greedy.py](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/TSP_Greedy.py): This computes a Hamiltonian cycle of G starting at a given node using a greedy approach. For each node after the first, the script selects an unvisited node that has the minimum edge weight with the current node. Once all nodes have been visited, the Hamiltonian cycle is completed by returning to the starting node.
[TSP_Christofides.py](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/TSP_Christofides.py): This computes a Hamiltonian cycle of G starting at a given node using Christofides algorithm. Christofides algorithm is guaranteed to find a Hamiltonian cycle with a total edge weight that is at worst 50% higher than the Hamiltonian cycle with the lowest total edge weight.


Step 2: Write a Python script that selects which of the 3 approaches from Step 1 to use to generate a Hamiltonian cycle for a graph G and its starting node. In an ideal world we would always use the brute force approach because it considers all possible Hamiltonian cycles and selects the best one. The issue here is with computation time: if G has too many nodes then the brute force approach takes too long to output an answer. For this reason the greedy approach and Christofides algorithm are also considered because they can each generate a Hamiltonian cycle much faster than the brute force approach when the number of nodes is large.

The question then becomes: "How do I know which of the 3 approaches I should use to generate a Hamiltonian cycle?" My investigation of this question can be seen in
[Analysis_of_TSP_Computation_Times.ipynb](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/Analysis_of_TSP_Computation_Times.ipynb). The summary of what is found in this notebook is that if graph G has at most 11 nodes then the brute force approach is most appropriate, as it should take no longer than 9 seconds to generate the Hamiltonian cycle. If G has just 12 nodes though then the brute force approach can take up to 71 second, which is arguably too long, so the brute force approach is by default not used when there are 12 or more nodes. 

The first visualization in this notebook shows that if graph G has at most 11 nodes then the brute force approach should take no longer than 9 seconds to generate the Hamiltonian cycle (a reasonable computation time), but if G has just 12 nodes then the computation time skyrockets up to 71 seconds (an unreasonable computation time). I concluded from this visualization that by default the brute force approach will be considered only for graphs with at most 11 nodes. 

The second visualization in this notebook shows that both the greedy approach and Christofides algorithm generate a Hamiltonian cycle nearly instantly even when there are 150 nodes in the graph. For this reason, when there are 12 or more nodes in G then two Hamiltonian cycles are generated - one using the greedy approach and one using Christofides algorithm - and the one with less total edge weight is selected.
