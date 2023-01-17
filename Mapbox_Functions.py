import requests
import mapbox
import polyline
import folium
import numpy as np
from math import sin, cos, sqrt, atan2, pi
from ATSP import atsp
from TSP import tsp


def distance_between_nodes(node_1, node_2, access_token):
    """
    Calculates the distance between node_1 and node_2 in meters using the Mapbox Directions API.
    :param node_1: A location on a map, represented by its coordinates as (latitude, longitude).
    :param node_2: A location on a map, represented by its coordinates as (latitude, longitude).
    :param access_token: A Mapbox API access token.
    :return: The distance between node_1 and node_2 in meters according to the Mapbox Directions API.
    """

    # Convert the nodes to strings that can be inserted into response.
    node_1 = f"{node_1[1]}, {node_1[0]}"
    node_2 = f"{node_2[1]}, {node_2[0]}"

    # Make the API request.
    response = requests.get("https://api.mapbox.com/directions/v5/mapbox/driving/" + node_1 + ";" + node_2 + ".json?access_token=" + access_token)

    # Parse the JSON response
    data = response.json()

    # Extract the distance from the response
    distance = data["routes"][0]["distance"]

    return distance

def haversine(node_1, node_2):
    """
    Calculates the distance between two points on the Earth's surface, while ignoring obstacles such as buildings. This
    will be used to calculate the distance between consecutive waypoints in the full route both to save API calls and
    also because Mapbox often does not return a distance value between consecutive waypoints.
    :param node_1: A location on a map, represented by its coordinates as (latitude, longitude).
    :param node_2: A location on a map, represented by its coordinates as (latitude, longitude).
    :return: The shortest distance along the Earth's surface between node_1 and node_2.
    """
    R = 6371000  # Earth's radius in meters.
    lat_1, lon_1 = node_1
    lat_2, lon_2 = node_2

    # The latitudes of node_1 and node_2 in radians.
    phi_1, phi_2 = lat_1 * pi / 180, lat_2 * pi / 180

    # The difference of the latitudes in radians.
    delta_phi = phi_2 - phi_1

    # The difference of the longitudes in radians.
    delta_lambda = (lon_2 - lon_1) * pi / 180

    # An intermediate value in the calculation.
    a = sin(delta_phi/2)**2 + cos(phi_1) * cos(phi_2) * sin(delta_lambda/2)**2

    return 2 * R * atan2(sqrt(a),sqrt(1-a))


def create_G(node_list, access_token):
    """
    Creates the graph G from the list of locations (nodes) the truck much visit.
    :param node_list: A list corresponding to all of the nodes that will be visited in the route. It is of the form
        [(latitude_1, longitude_1), (latitude_2, longitude_2), ...]. Note that the nodes do not need to be ordered
        according to the order that they will be visited in the route; the generate_route() function computes the ordering.
    :param access_token: A Mapbox API access token.
    :return: A graph G that can be input into the atsp() and tsp() functions.
    """

    # Count the number of nodes and initialize G.
    n = len(node_list)
    G = {}

    # Generate the diagonal of 0's in G; each node has a distance of 0 to itself.
    for i in range(n):
        node_i = node_list[i]
        G[node_i] = {node_i: 0}

    # Generate the entries of G above the diagonal using the Mapbox API.
    for i in range(n):
        node_i = node_list[i]
        for j in range(i+1, n):
            node_j = node_list[j]
            G[node_i][node_j] = distance_between_nodes(node_i, node_j, access_token)

    # Generate the entries of G below the diagonal by symmetry with the entries above the diagonal.
    for i in range(1, n):
        node_i = node_list[i]
        for j in range(i):
            node_j = node_list[j]
            G[node_i][node_j] = G[node_j][node_i]

    return G


def generate_route(G, start, is_asymmetric=True):
    """
    The function which generates the full route. The selected route depends on whether or not the truck needs to end
    at the same location that it started.
    :param G: A graph for which we want to compute a Hamiltonian cycle or path.
    :param start: The starting node (location) of the truck's journey.
    :param is_asymmetric: If set to True then the truck will not return to its starting node (location) once all of the
        nodes (locations) have been visited. If set to False the truck will return to its starting node (location) once
        all of the nodes (locations) have been visited, so the last node and start node will be equal.
    :return: A Hamiltonian cycle or path of G.
    """
    if is_asymmetric:
        return atsp(G, start)
    else:
        return tsp(G, start)

def ordered_node_list(route):
    """
    This computes the order that the nodes (locations) will be traveled in the Hamiltonian cycle or path of G. This is
    needed for generate_map() so that the nodes can be labeled correctly in the displayed interactive map.
    :param route:
    :return:
    """
    # We just want the route, not the total distance of the route.
    route_without_total_distance = route[1]

    # Extract all nodes but the last in the route, in order.
    ordered_nodes = [edge_list[0] for edge_list in route_without_total_distance]

    # Include the last node in the route.
    ordered_nodes.append(route_without_total_distance[-1][1])

    return ordered_nodes


def waypoint_list_between_node_pair(node_1, node_2, access_token):
    """
    Calculates a list of waypoints (i.e. intermediate points) between locations node_1 and node_2.
    :param node_1: A location on a map, represented by its coordinates as (latitude, longitude).
    :param node_2: A location on a map, represented by its coordinates as (latitude, longitude).
    :param access_token: A Mapbox API access token.
    :return: A list of waypoints along the subroute from node_1 to node_2. It is of the form
        [(latitude_1, longitude_1), (latitude_2, longitude_2), ...].
    """

    # Extract the coordinates of node_1 and node_2.
    node_1_string = f"{node_1[1]}, {node_1[0]}"
    node_2_string = f"{node_2[1]}, {node_2[0]}"

    # Extract the list of waypoints representing the shortest route from node_1 to node_2.
    # Each item in the list corresponds to 1 waypoint and is a tuple of the form (latitude, longitude).
    response = requests.get("https://api.mapbox.com/directions/v5/mapbox/driving/" + node_1_string + ";" + node_2_string + ".json?access_token=" + access_token)
    route = response.json()['routes'][0]
    encoded_polyline = route['geometry']
    waypoint_list = polyline.decode(encoded_polyline)

    return waypoint_list


def waypoint_list_full_route(full_route, access_token):
    """
    Calculates a list of waypoints (i.e. intermediate points) along the Hamiltonian cycle or path.
    :param full_route: The output of generate_route(G, start, is_asymmetric).
    :param access_token: A Mapbox API access token.
    :return: A list of waypoints along the full Hamiltonian cycle or path. It is of the form
        [(latitude_1, longitude_1), (latitude_2, longitude_2), ...].
    """

    # Initialize the list in which the waypoints will be stored.
    waypoint_list_full = []

    # full_route[1] gives the Hamiltonian cycle or path.
    # full_route[1][i] gives edge i in the Hamiltonian cycle or path.
    # full_route[1][i][0] and full_route[1][i][1] give the nodes of edge i in the Hamiltonian cycle or path.
    n = len(full_route[1])
    for i in range(n):
        node_i = full_route[1][i][0]
        node_i_plus_1 = full_route[1][i][1]
        waypoint_list_full += waypoint_list_between_node_pair(node_i, node_i_plus_1, access_token)

    return waypoint_list_full


def cumulative_distance_along_waypoints(waypoint_list_full_route, access_token):
    """
    This is used to predict when to warn the truck driver that he or she will need to fill up on gas.
    :param waypoint_list_full_route: A list of waypoints along the full Hamiltonian cycle or path. It is of the form
        [(latitude_1, longitude_1), (latitude_2, longitude_2), ...].
    :param access_token:
    :return: A list with one entry for each waypoint in the full route, where entry i is the cumulative distance (in meters) traveled
    in the full route up to that waypoint.
    """

    n = len(waypoint_list_full_route)

    # Initialize the cumulative distance at 0, and also the list which will store the cumulative_distances.
    cumulative_distance = 0
    cumulative_distance_list = [0]

    # Calculate the cumulative distance of the route at each waypoint and store it in the list.
    for i in range(1, n):
        # To save API calls perhaps replace distance_between_nodes with haversine.
        cumulative_distance += haversine(waypoint_list_full_route[i - 1], waypoint_list_full_route[i])
        cumulative_distance_list.append(cumulative_distance)

    return cumulative_distance_list


def predict_waypoints_where_to_search_for_gas(cumulative_distance_along_waypoints, waypoint_list_full_route, start_tank_kms, full_tank_kms, min_tank_tolerance_kms=20):
    """
    This function predicts when the truck will need to begin to look for a gas station. This function assumes that each
    time the truck stops at a gas station the tank is filled completely. Moreover, it assumes that the truck has to go off
    the main route to reach the gas station, and that as a consequence it spends 5km leaving the main route and 5km returning
    to the main route before continuing the journey to the next node.
    :param cumulative_distance_along_waypoints: A list with one entry for each waypoint in the full route, where entry i
        is the cumulative distance (in meters) traveled in the full route up to that waypoint.
    :param waypoint_list_full_route: A list of waypoints along the full Hamiltonian cycle or path. It is of the form
        [(latitude_1, longitude_1), (latitude_2, longitude_2), ...].
    :param start_tank_kms: How many kilometers worth of gas the truck driver has in the tank at the beginning of the route.
    :param full_tank_kms: The maximum distance (in kilometers) the truck can be driven when the gas tank is full.
    :param min_tank_tolerance_kms: The gas driver is planning their route such that they never have less than this many
        kilometers worth of gas in their tank. Typically it is >0 because it would be risky always arriving at gas
        stations with just enough gas to make it there.
    :return: A list of waypoints representing predicted locations where the truck driver should start looking for gas.
        It is of the form [(latitude_1, longitude_1), (latitude_2, longitude_2), ...].
    """

    # Convert cumulative_distance_along_waypoints to a NumPy array so that broadcasting can be used.
    A = np.array(cumulative_distance_along_waypoints)
    n = len(A)

    # Convert from kilometers to meters for consistency with Mapbox, which returns distances in meters.
    max_initial_distance_before_search_gas = 1000 * (start_tank_kms - min_tank_tolerance_kms - 2*5)
    max_distance_before_searching_gas_with_full_tank = 1000 * (full_tank_kms - min_tank_tolerance_kms - 2*5)

    index = 0
    index_list = []

    # Search for the furthest waypoint the truck can make it to from the starting node until it must fill up on gas.
    # When that waypoint is reached, subtract the distance traveled from the cumulative distance for all of the
    # remaining waypoints.
    for i in range(1, n):
        if A[i] <= max_initial_distance_before_search_gas:
            continue
        else:
            index = i - 1
            index_list.append(index)
            A -= A[i - 1]
            break

    # Search for the furthest waypoint the truck can make it from its starting node until it must fill up on gas.
    # When that waypoint is reached, subtract the distance traveled from the cumulative distance for all of the
    # remaining waypoints.

    # From the last waypoint where the gas tanked was filled up, search for the furthest waypoint the truck can make it to
    # until it must fill up on gas again. When that waypoint is reached, subtract the distance traveled since the last
    # gas waypoint from the cumulative distance for all of the remaining waypoints. Repeat until the end of the journey.
    for i in range(index, n):
        if A[i] <= max_distance_before_searching_gas_with_full_tank:
            continue
        else:
            index = i - 1
            index_list.append(index)
            A -= A[i - 1]
            continue

    # Extract the waypoints where it is predicted that a gas tank fill up is needed.
    waypoints = list(np.array(waypoint_list_full_route)[index_list])

    return waypoints


def generate_map(access_token, node_list, start, start_tank_kms, full_tank_kms, min_tank_tolerance_kms=20, is_asymmetric=True):
    """
    This function generates an interactive map of the Hamiltonian cycle or path.
    :param access_token: A Mapbox API access token.
    :param node_list: A list corresponding to all of the nodes that will be visited in the route. It is of the form
        [(latitude_1, longitude_1), (latitude_2, longitude_2), ...]. Note that the nodes do not need to be ordered
        according to the order that they will be visited in the route; the generate_route() function computes the ordering.
    :param start: The starting node (location) of the truck's journey.
    :param start_tank_kms: How many kilometers worth of gas the truck driver has in the tank at the beginning of the route.
    :param full_tank_kms: The maximum distance (in kilometers) the truck can be driven when the gas tank is full.
    :param min_tank_tolerance_kms: The gas driver is planning their route such that they never have less than this many
        kilometers worth of gas in their tank. Typically it is >0 because it would be risky always arriving at gas
        stations with just enough gas to make it there.
    :param is_asymmetric: If set to True then the truck will not return to its starting node (location) once all of the
        nodes (locations) have been visited. If set to False the truck will return to its starting node (location) once
        all of the nodes (locations) have been visited, so the last node and start node will be equal.
    :return: An interactive map of the Hamiltonian cycle or path.
    """

    # Call the functions that are used to generate the interactive map.
    G = create_G(node_list, access_token)
    full_route = generate_route(G, start, is_asymmetric)
    ordered_nodes = ordered_node_list(full_route)
    waypoint_list_full = waypoint_list_full_route(full_route, access_token)
    cumulative_distance = cumulative_distance_along_waypoints(waypoint_list_full, access_token)
    waypoints_where_to_search_for_gas = predict_waypoints_where_to_search_for_gas(cumulative_distance, waypoint_list_full, start_tank_kms, full_tank_kms, min_tank_tolerance_kms)

    # Extract the first point of the route
    first_point = waypoint_list_full[0]

    # Create a new map.
    m = folium.Map(location=[first_point[1], first_point[0]], zoom_start=13)

    # Add the route to the map.
    folium.PolyLine(waypoint_list_full, color="purple", weight=2.5, opacity=1).add_to(m)

    # For the second to second-last nodes, create a marker on the map and label it 'delivery point'.
    for i in range(1, len(ordered_nodes) - 1):
        folium.Marker(
            location=[ordered_nodes[i][0], ordered_nodes[i][1]],
            popup=folium.Popup(f'Node {i + 1} {ordered_nodes[i][0], ordered_nodes[i][1]}: delivery point', max_width=600),
            icon=folium.Icon(color='blue', icon='marker')
        ).add_to(m)

    # For the asymmetric case, create a marker on the map for the first node labeled 'start of route', and create a
    # marker on the map for the last node labeled 'last delivery point and end of route'.
    if is_asymmetric:

        folium.Marker(
            location=[ordered_nodes[0][0], ordered_nodes[0][1]],
            popup=folium.Popup(f'Node 1 {ordered_nodes[0][0], ordered_nodes[0][1]}: start of route', max_width=600),
            icon=folium.Icon(color='blue', icon='marker')
        ).add_to(m)

        folium.Marker(
            location=[ordered_nodes[len(ordered_nodes) - 1][0], ordered_nodes[len(ordered_nodes) - 1][1]],
            popup=folium.Popup(f'Node {len(ordered_nodes)} {ordered_nodes[len(ordered_nodes) - 1][0], ordered_nodes[len(ordered_nodes) - 1][1]}: last delivery point and end of route', max_width=600),
            icon=folium.Icon(color='blue', icon='marker')
        ).add_to(m)

    # For the symmetric case, create a marker on the map for the first/last node labeled 'start and end of route'.
    if not is_asymmetric:
        folium.Marker(
            location=[ordered_nodes[0][0], ordered_nodes[0][1]],
            popup=folium.Popup(f'First and last node {ordered_nodes[0][0], ordered_nodes[0][1]}: start and end of route', max_width=600),
            icon=folium.Icon(color='blue', icon='marker')
        ).add_to(m)

    # For each predicted gas station, create a marker on the map labeled 'Look for gas station!'.
    for waypoint in waypoints_where_to_search_for_gas:
        folium.Marker(
            location=[waypoint[0], waypoint[1]],
            popup=folium.Popup('Look for gas station!', max_width=600),
            icon=folium.Icon(color='red', icon='marker')
        ).add_to(m)

    # Display the map
    return m