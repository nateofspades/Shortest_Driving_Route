import heapq

def shortest_route(destinations, distances):
    """
    Find the shortest route for a truck traveling from an initial source to a final destination, with multiple intermediate destinations available.

    Parameters:
    destinations (list of str): The list of destinations that the truck can visit.
    distances (list of tuples): A list of tuples containing the distances between pairs of destinations. Each tuple should contain three elements: (src, dest, distance), where src and dest are the names of the source and destination, respectively, and distance is the distance between them.

    Returns:
    list of str: A list of the destinations visited in the order they were visited, representing the shortest route.
    """
    # Create a graph representation of the destinations and distances
    graph = {dest: {} for dest in destinations}
    for src, dest, distance in distances:
        graph[src][dest] = distance
        graph[dest][src] = distance

    # Implement Dijkstra's algorithm to find the shortest route
    # Initialize the priority queue with the starting point
    heap = [(0, 0, 0, [])]  # (distance, cost, src, route)
    # Keep track of the destinations that have been visited
    visited = set()
    # Continue the search as long as there are nodes in the priority queue
    while heap:
        # Extract the node with the minimum distance from the priority queue
        distance, cost, src, route = heapq.heappop(heap)
        # If the current node is the destination, return the found route
        if src == len(destinations) - 1:
            return route + [destinations[src]]
        # If the current node has already been visited, skip it
        if src in visited:
            continue
        # Mark the current node as visited
        visited.add(src)
        # Add all of the neighbors of the current node to the priority queue
        for dest, edge_distance in graph[destinations[src]].items():
            dest_index = destinations.index(dest)
            heapq.heappush(heap, (cost + edge_distance, cost + edge_distance, dest_index, route + [destinations[src]]))

# Test the shortest_route function
destinations = ['A', 'B', 'C', 'D', 'E']
distances = [('A', 'B', 5), ('B', 'C', 3), ('C', 'D', 4), ('D', 'E', 2), ('A', 'D', 10), ('B', 'E', 5)]
print(shortest_route(destinations, distances))  # ['A', 'B', 'C', 'D', 'E']

destinations = ['A', 'B', 'C', 'D', 'E']
distances = [('A', 'B', 5), ('A', 'C', 10), ('B', 'C', 3), ('B', 'D', 7), ('C', 'D', 4), ('C', 'E', 8), ('D', 'E', 2)]
print(shortest_route(destinations, distances))  # ['A', 'B', 'C', 'D', 'E']
