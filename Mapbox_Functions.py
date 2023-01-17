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

    # Generate the entries of G above the diagonal using API.
    for i in range(n):
        node_i = node_list[i]
        for j in range(i + 1, n):
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
    :param is_asymmetric: If set to true then the truck will not return to its starting node (location) once all of the
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
    route is the output of generate_route
    """
    # We just want the route, not the total distance of the route.
    route_without_total_distance = route[1]

    # Extract all but the last node in the route, in order.
    ordered_nodes = [edge_list[0] for edge_list in route_without_total_distance]

    # Include the last node in the route.
    ordered_nodes.append(route_without_total_distance[-1][1])

    return ordered_nodes


def waypoint_list_between_node_pair(node_1, node_2, access_token):
    """
    Makes Mapbox API calls to determine the shortest route between node_1 and node_2, as well as the length of this route.
    node_1 and node_2 are each a tuple of the form (longitude, latitude)
    """

    # Extract the coordinates of node_1 and node_2.
    node_1_string = f"{node_1[1]}, {node_1[0]}"
    node_2_string = f"{node_2[1]}, {node_2[0]}"

    # Extract the list of waypoints representing the shortest route from node_1 to node_2.
    # Each item in the list corresponds to 1 waypoint and is a tuple of the form (latitude, longitude).
    response = requests.get(
        "https://api.mapbox.com/directions/v5/mapbox/driving/" + node_1_string + ";" + node_2_string + ".json?access_token=" + access_token)
    route = response.json()['routes'][0]
    encoded_polyline = route['geometry']
    waypoint_list = polyline.decode(encoded_polyline)

    #     # Include the node_1 at the beginning of the list and node_2 at the end of the list.
    #     waypoint_list.insert(0, node_1)
    #     waypoint_list.append(node_2)

    return waypoint_list


def waypoint_list_full_route(full_route, access_token):
    waypoint_list_full = []

    n = len(full_route[1])
    for i in range(n):
        node_i = full_route[1][i][0]
        node_i_plus_1 = full_route[1][i][1]
        waypoint_list_full += waypoint_list_between_node_pair(node_i, node_i_plus_1, access_token)

    return waypoint_list_full


# def cumulative_distance_along_waypoints(waypoint_list_full_route, access_token):
#     n = len(waypoint_list_full_route)
#     cumulative_distance = 0
#     cumulative_distance_list = [0]
#
#     for i in range(1, n):
#         # To save API calls perhaps replace distance_between_nodes with haversine.
#         cumulative_distance += distance_between_nodes(waypoint_list_full_route[i - 1], waypoint_list_full_route[i], access_token)
#         cumulative_distance_list.append(cumulative_distance)
#
#     return cumulative_distance_list


def cumulative_distance_along_waypoints(waypoint_list_full_route, access_token):
    n = len(waypoint_list_full_route)
    cumulative_distance = 0
    cumulative_distance_list = [0]

    for i in range(1, n):
        # To save API calls perhaps replace distance_between_nodes with haversine.
        cumulative_distance += haversine(waypoint_list_full_route[i - 1], waypoint_list_full_route[i])
        cumulative_distance_list.append(cumulative_distance)

    return cumulative_distance_list



def predict_waypoints_where_to_search_for_gas(cumulative_distance_along_waypoints, waypoint_list_full_route, start_tank_kms, full_tank_kms, min_tank_tolerance_kms=20):
    """
    This function assumes that each time the truck stops at a gas station it fills its tank completely.
    Moreover, it assumes that the truck had to go off the main route to reach the gas station, and that as a consequence it
    spends 5km leaving the main route and 5km returning to the main route before continuing its journey to the next node.
    """
    A = np.array(cumulative_distance_along_waypoints)
    n = len(A)

    # Convert from kilometers to meters for consistency with Mapbox, which returns distances in meters.
    max_initial_distance_before_search_gas = 1000*(start_tank_kms - min_tank_tolerance_kms - 2*5)
    max_distance_before_searching_gas_with_full_tank = 1000*(full_tank_kms - min_tank_tolerance_kms - 2*5)

    index = 0
    index_list = []

    for i in range(1, n):
        if A[i] <= max_initial_distance_before_search_gas:
            continue
        else:
            index = i - 1
            index_list.append(index)
            A -= A[i - 1]
            #print(A, index_list, '\n')
            break

    for i in range(index, n):
        if A[i] <= max_distance_before_searching_gas_with_full_tank:
            continue
        else:
            index = i - 1
            index_list.append(index)
            A -= A[i - 1]
            #print(A, index_list, '\n')
            continue

    waypoints = list(np.array(waypoint_list_full_route)[index_list])

    return waypoints


def generate_map(access_token, node_list, start, start_tank_kms, full_tank_kms, min_tank_tolerance_kms=20, is_asymmetric=True):
    """
    Putting it all together.
    """
    G = create_G(node_list, access_token)
    full_route = generate_route(G, start, is_asymmetric)
    ordered_nodes = ordered_node_list(full_route)
    waypoint_list_full = waypoint_list_full_route(full_route, access_token)
    cumulative_distance = cumulative_distance_along_waypoints(waypoint_list_full, access_token)
    waypoints_where_to_search_for_gas = predict_waypoints_where_to_search_for_gas(cumulative_distance, waypoint_list_full, start_tank_kms, full_tank_kms, min_tank_tolerance_kms)

    # Extract the first point of the route
    first_point = waypoint_list_full[0]

    # Create a new map
    m = folium.Map(location=[first_point[1], first_point[0]], zoom_start=13)

    # Add the route to the map
    folium.PolyLine(waypoint_list_full, color="purple", weight=2.5, opacity=1).add_to(m)

    for i in range(1, len(ordered_nodes) - 1):
        folium.Marker(
            location=[ordered_nodes[i][0], ordered_nodes[i][1]],
            popup=folium.Popup(f'Node {i + 1} {ordered_nodes[i][0], ordered_nodes[i][1]}: delivery point', max_width=600),
            icon=folium.Icon(color='blue', icon='marker')
        ).add_to(m)

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

    if not is_asymmetric:
        folium.Marker(
            location=[ordered_nodes[0][0], ordered_nodes[0][1]],
            popup=folium.Popup(f'First and last node {ordered_nodes[0][0], ordered_nodes[0][1]}: start and end of route', max_width=600),
            icon=folium.Icon(color='blue', icon='marker')
        ).add_to(m)

    for waypoint in waypoints_where_to_search_for_gas:
        folium.Marker(
            location=[waypoint[0], waypoint[1]],
            popup=folium.Popup('Look for gas station!', max_width=600),
            icon=folium.Icon(color='red', icon='marker')
        ).add_to(m)

    # Display the map
    return m