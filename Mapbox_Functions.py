# import json
# import requests
# import mapbox
# import mapboxgl
# import polyline
# import geopy
# import folium
# import math
# import numpy as np
# import pprint
# from math import sin, cos, sqrt, atan2, pi
# from ATSP import atsp

def h(x):
    return x**2

access_token = 'pk.eyJ1IjoibmF0aGFuYnVybnNkcyIsImEiOiJjbGN1cnJtYXIwM3J5M29uOGVxODQ5YzZ6In0.yZoDdvT20-BYJoi8KOxvvA'

def distance_between_nodes(node_1, node_2, access_token):
    """
    This function will be used in the creation of G using the create_G function I made in Pycharm on Jan. 14)
    """
    # Convert the nodes to strings that can be inserted into response.
    node_1 = f"{node_1[1]}, {node_1[0]}"
    node_2 = f"{node_2[1]}, {node_2[0]}"

    # Make the API request.
    response = requests.get(
        "https://api.mapbox.com/directions/v5/mapbox/driving/" + node_1 + ";" + node_2 + ".json?access_token=" + access_token)

    # Parse the JSON response
    data = response.json()

    # Extract the distance from the response
    distance = data["routes"][0]["distance"]

    return distance


def create_G(node_list, access_token):
    """
    Nodes is a list, where each element corresponds to one node.
    """

    n = len(node_list)
    G = {}

    # Generate the diagonal of 0's.
    for i in range(n):
        node_i = node_list[i]
        G[node_i] = {node_i: 0}

    # Generate the entries of G above the diagonal using API.
    for i in range(n-1):
        node_i = node_list[i]
        node_i_edges = {}
        for j in range(i, n):
            node_j = node_list[j]
            node_i_edges[node_j] = distance_between_nodes(node_i, node_j, access_token) #distances_temp[node_i][node_j]   # the distance between node_i and node_j; replace this with api call
        G[node_i] = node_i_edges

    # Generate the entries of G below the diagonal by symmetry with the entries above the diagonal.
    for i in range(1, n):
        node_i = node_list[i]
        for j in range(i):
            node_j = node_list[j]
            G[node_i][node_j] = G[node_j][node_i]

    return G


def generate_route(G, start, is_asymmetric=True):
    """
    The function which generates the full route.
    """
    if is_asymmetric:
        return atsp(G, start)
    else:
        return tsp(G, start)


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

    return waypoint_list


def waypoint_list_full_route(full_route, access_token):
    waypoint_list_full = []

    n = len(full_route[1])
    for i in range(n):
        node_i = full_route[1][i][0]
        node_i_plus_1 = full_route[1][i][1]
        waypoint_list_full += waypoint_list_between_node_pair(node_i, node_i_plus_1, access_token)

    return waypoint_list_full


def cumulative_distance_along_waypoints(waypoint_list_full_route, access_token):
    n = len(waypoint_list_full_route)
    cumulative_distance = 0
    cumulative_distance_list = [0]

    for i in range(1, n):
        # To save API calls perhaps replace distance_between_nodes with haversine.
        cumulative_distance += distance_between_nodes(waypoint_list_full_route[i - 1], waypoint_list_full_route[i],
                                                      access_token)
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
    max_distance_before_searching_gas = full_tank_kms - min_tank_tolerance_kms - 2 * 5

    index = 0
    index_list = []
    for i in range(index, n):
        if A[i] < max_distance_before_searching_gas:
            continue
        else:
            index = i - 1
            index_list.append(index)
            A -= A[i - 1]
            # print(cdaw, index_list, '\n')
            continue

    waypoints = list(np.array(waypoint_list_full_route)[index_list])

    return waypoints


### NEED TO MAKE THIS A FUNCTION

# Extract the first point of the route
# first_point = waypoint_list_full_route[0]
#
# # Create a new map
# m = folium.Map(location=[first_point[1], first_point[0]], zoom_start=13)
#
# # Add the route to the map
# folium.PolyLine(waypoint_list_full_route, color="red", weight=2.5, opacity=1).add_to(m)
#
# for node in node_list:
#     folium.Marker(
#         location=[node[0], node[1]],
#         popup='One of the delivery spots.',
#         icon=folium.Icon(color='red', icon='marker')
#     ).add_to(m)
#
# for waypoint in waypoints_where_to_search_for_gas:
#     folium.Marker(
#         location=[waypoint[0], waypoint[1]],
#         popup='Look for a gas station.',
#         icon=folium.Icon(color='red', icon='info-sign')
#     ).add_to(m)
#
# # Display the map
# m