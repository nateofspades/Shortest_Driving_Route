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


Step 2: Write a Python script that selects which of the 3 Hamiltonian cycles to use 
