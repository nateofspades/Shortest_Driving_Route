from ATSP import atsp

def calculate_nearest_gas_stations(G):
    """
    This function takes a graph as input and outputs a dictionary where the keys are the nodes of G and the value
    for a key is a tuple of length 2: the first element of a tuple is the nearest gas station to the node, the second is the distance
    between the gas station and the node.
    Example for node    'D': ('nearest_gas_station', 17)
    """

G = {
    'A':{'A':2, 'B':6}
}
G['C'] = 10
print(G)

def update_G(G, nodes_already_visited):
    """
    This helper function will be within the body of the function that computes the route (because it needs access to nodes_already_visited).
    When G visits a gas station the graph needs to be recomputed to figure out how to best get to the nodes_not_yet_visited.
    (We will worry about the possibility of G going off track and the route needing to be recomputed at a later moment.)
    """

def max_possible_distance(current_gas_tank_proportion, ...):
    """
    Based on how much gas is in the tank and the rate at which gas is consumed per mile, this will calculate how far the truck can
    go until it runs out of gas.
    """

def compute_next_subroute(remaining_nodes, current_node, current_gas_tank_proportion, min_acceptable_gas_tank_proportion):



def compute_route(G, start, current_gas_tank_proportion, min_acceptable_gas_tank_proportion):
    """
    """

    gas_stations = calculate_nearest_gas_stations(G)
    route_and_total_weight = atsp(G, start)
    route = route_and_total_weight[1]
    remaining_nodes = list(G.keys())

    # Calculate furthest we can go given current gas situation
    mpd = max_possible_distance(current_gas_tank_proportion)


    # Travel to the furthest mandatory node possible such that you would furthermore be able to reach its gas station.
    current_node = route[0][0]
    subroute_nodes = [current_node]
    subroute_length = 0 # length of path from current node to furthest mandatory node it can reach such that it would furthermore be able to reach its gas station (set to 0 because we are assuming we can get from the current node to the nearest gas station)
    for edge in route:
        if subroute_length + edge[2] + distance_from_edge[1]_to_its_nearest_gas_station    < mpd:
            subroute_nodes.append(edge[1])
            subroute_length += edge[2]
    subroute_nodes.append(#nearest_gas_station_to_last_node)
    # Now we should have a list up to the furthest mandatory node we can reach followed by the last node's nearest gas station.

    # Convert subroute_nodes list to dictionary so that it can be input into atsp()

    subroute_dictionary = {}







# Example initial route for G
route_and_total_weight = (12, [('A', 'C', 3), ('C', 'E', 1), ('E', 'D', 4), ('D', 'B', 4)])
route =                       [('A', 'C', 3), ('C', 'E', 1), ('E', 'D', 4), ('D', 'B', 4)]























