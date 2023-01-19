# Shortest_Driving_Route

Suppose you are a trucker who needs to make deliveries in multiple locations. Two questions you might naturally ask yourself are:

1. "**What is the shortest route I can take?**"
2. "**At which point(s) along the route should I begin to look for a gas station?**"

The focus of this project is to answer both of these questions. 

Screenshots of two examples of the end result of this project can be seen at the first two links below:

[Mapbox_Example_TSP_Screenshots](https://github.com/nateofspades/Shortest_Driving_Route/tree/master/Mapbox/Mapbox_Example_TSP_Screenshots). This consists of 4 screenshots of a trucker route that begins in Quebec City and makes a delivery in each of Montreal, Ottawa, Kingston and London before returning to Quebec City. Each of these locations are labeled in **blue**. The map also labels 3 suggested locations for when the driver should begin to look for a gas station in **red**. 

[Mapbox_Example_ATSP_Screenshots](https://github.com/nateofspades/Shortest_Driving_Route/tree/master/Mapbox/Mapbox_Example_ATSP_Screenshots): This is another set of 4 screenshots of a route that begins in Quebec City and makes a delivery in each of Montreal, Ottawa, Kingston and London. In this route the trucker does not return to the starting point, Quebec city, after visiting the last delivery point in London. The locations are labeled in **blue** and the suggested locations for when the driver should begin to look for a gas station in **red**. 

[Mapbox_Example_ATSP_Screenshots](https://github.com/nateofspades/Shortest_Driving_Route/tree/master/Mapbox/Mapbox_Example_ATSP_Screenshots): This consists of 4 screenshots of a route that begins in Quebec City and makes a delivery in each of Montreal, Ottawa, Kingston and London - where the route ends. Each of these locations are labeled in **blue**. The map also labels 2 suggested locations for when the driver should begin to look for a gas station in **red**. 

This project is a direct application of the **Traveling Salesman Problem** using the **Mapbox Directions API**. Here's what I did:

## Step 1a - Traveling Salesman Problem Using 3 Approaches:

Write Python scripts that compute a cycle of a weighted complete graph G which starts at a given node and passes through all of the nodes of G. A cycle of G which passes through all nodes of G is called a **Hamiltonian cycle**. Each node can be thought of as a location that the trucker must visit, and the edge weight between two nodes is the distance between the two nodes.

There are 3 such scripts, each corresponding to a different way that a Hamiltonian cycle can be computed: </br>
[TSP_Brute_Force.py](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/TSP_Brute_Force.py): This computes all of the possible Hamiltonian cycles of G starting at a given node and selects one with the minimum total edge weight.
[TSP_Christofides.py](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/TSP_Christofides.py): This computes a Hamiltonian cycle of G starting at a given node using Christofides algorithm. Christofides algorithm is guaranteed to find a Hamiltonian cycle with a total edge weight that is at worst 50% higher than the Hamiltonian cycle with the lowest total edge weight.
[TSP_Greedy.py](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/TSP_Greedy.py): This computes a Hamiltonian cycle of G starting at a given node using a greedy approach. For each node after the first, the script selects an unvisited node that has the minimum edge weight with the current node. Once all nodes have been visited, the Hamiltonian cycle is completed by returning to the starting node.

## Step 2a - Selecting Best Traveling Salesman Problem Approach:

[TSP.py](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/TSP.py): This Python script selects which of the 3 approaches from Step 1a to use to generate a Hamiltonian cycle for a graph G and its starting node. In an ideal world we would always use the brute force approach because it considers all possible Hamiltonian cycles and selects the best one. The issue here is with computation time: if G has too many nodes then the brute force approach takes too long to output an answer. For this reason the greedy approach and Christofides algorithm are also considered because they can each generate a Hamiltonian cycle much faster than the brute force approach when the number of nodes is large.

The question then becomes: "How do I know which of the 3 approaches I should use to generate a Hamiltonian cycle?" My investigation of this question can be seen in
[Analysis_of_TSP_Computation_Times.ipynb](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/Analysis_of_TSP_Computation_Times.ipynb). In this notebook I used [Create_Random_Graph.py](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/Create_Random_Graph.py) to generate random graphs of various sizes that can be input into the 3 approaches above so that I could determine worst-case computation times. 

The first visualization in this notebook shows that if graph G has at most 11 nodes then the brute force approach should take no longer than 9 seconds to generate the Hamiltonian cycle (a reasonable computation time), but if G has just 12 nodes then the computation time skyrockets up to 71 seconds (an unreasonable computation time). I concluded from this visualization that **by default the brute force approach will be considered only for graphs with at most 11 nodes**. 

The second visualization in this notebook shows that both the greedy approach and Christofides algorithm generate a Hamiltonian cycle nearly instantly even when there are 150 nodes in the graph. In other words, even if the trucker has to visit as many as 150 locations, both the greedy approach and Christofides algorithm could provide a recommended route nearly instantly. For this reason, **if there are 12 or more nodes in G then two Hamiltonian cycles are generated - one using the greedy approach and one using Christofides algorithm - and the one with less total edge weight (i.e. less total distance traveled) is selected**.

## Step 1b - Asymmetric Traveling Salesman Problem Using 3 Approaches:

This is similar to Step 2 except that now we are interested in creating a **Hamiltonian path** instead of a Hamiltonian cycle. The difference is that now we are no longer interested in returning to the starting node after the last node has been visited. 

There are 3 such scripts, each corresponding to a different way that a Hamiltonian path can be computed: </br>
[ATSP_Brute_Force.py](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/ATSP_Brute_Force.py): This computes all of the possible Hamiltonian paths of G starting at a given node and selects one with the minimum total edge weight.
[ATSP_Christofides.py](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/ATSP_Christofides.py): This computes the Hamiltonian cycle generated by TSP_Christofides.py and removes the last edge.
[ATSP_Greedy.py](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/ATSP_Greedy.py): This computes the Hamiltonian cycle generated by TSP_Greedy.py and removes the last edge.

## Step 2b - Selecting Best Asymmetric Traveling Salesman Problem Approach:

[ATSP.py](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/ATSP.py): This Python script selects which of the 3 approaches from Step 1b to use to generate a Hamiltonian path for a graph G and its starting node. The selection process is analogous to the selection process for a Hamiltonian cycle found in Step 2a. 


## Step 3 - Creating Mapbox Functions

Mapbox is a company that provides a platform for creating and using maps.

[Mapbox_Functions.py](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/Mapbox/Mapbox_Functions.py): The purpose of this script was to build the function **generate_map()** found at the bottom of the script. The generate_map() function generates an interactive map which displays the suggested route a trucker should take, as well as suggestions for when the driver should begin looking for gas stations, given the function following inputs:

access_token: A Mapbox Directions API access token.
node_list: A list corresponding to all of the nodes (i.e. locations) that will be visited in the route.
start: The starting node (i.e. starting location) of the truck's journey.
start_tank_kms: How many kilometers worth of gas the truck driver has in the tank at the beginning of the route.
full_tank_kms: The maximum distance (in kilometers) the truck can be driven when the gas tank is full.
min_tank_tolerance_kms: The gas driver is planning their route such that they never have less than this many kilometers worth of gas in their tank. (Typically it is >0 because it would be risky always arriving at gas stations with just enough gas to make it there.)
is_asymmetric: If set to False then the truck will use Step 2a to generate the Hamiltonian cycle route; the truck will return to its starting node (i.e. starting location) once all of the nodes (i.e. locations) have been visited. If set to True then the truck will use Step 2b to generate the Hamiltonian path route; the truck will not return to its starting node (i.e. starting location) once all of the nodes (i.e. locations) have been visited.

## Step 4a - Example of Hamiltonian Cycle Trucker Route

[Mapbox_Example_TSP_Code.ipynb](https://github.com/nateofspades/Shortest_Driving_Route/blob/master/Mapbox/Mapbox_Example_TSP_Code.ipynb): This notebook shows an example of how to use the generate_map() function from Step 3. It generates a trucker route that begins in Quebec City and makes a delivery in each of Montreal, Ottawa, Kingston and London before returning to Quebec City. You can see screenshots of the interactive output in 
[Mapbox_Example_TSP_Screenshots](https://github.com/nateofspades/Shortest_Driving_Route/tree/master/Mapbox/Mapbox_Example_TSP_Screenshots). Each of the locations are labeled in **blue**. The map also labels 3 suggested locations for when the driver should begin to look for a gas station in **red**. 

## Step 4b - Example of Hamiltonian Path Trucker Route
[Mapbox_Example_ATSP_Screenshots](https://github.com/nateofspades/Shortest_Driving_Route/tree/master/Mapbox/Mapbox_Example_ATSP_Screenshots): This notebook shows an example of how to use the generate_map() function from Step 3. It generates a trucker route that begins in Quebec City and makes a delivery in each of Montreal, Ottawa, Kingston and London - where the route ends. You can see screenshots of the interactive output in [Mapbox_Example_ATSP_Screenshots](https://github.com/nateofspades/Shortest_Driving_Route/tree/master/Mapbox/Mapbox_Example_ATSP_Screenshots). Each of the locations are labeled in **blue**. The map also labels 2 suggested locations for when the driver should begin to look for a gas station in **red**. 
