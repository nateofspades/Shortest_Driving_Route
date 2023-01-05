import itertools
import time

def tsp_brute_force(destinations, distances, start):
    # Get all permutations of the destinations
    permutations = itertools.permutations(destinations)

    # Set the minimum distance to a very large number
    min_distance = float('inf')

    # Set the best path to None
    best_path = None

    # Iterate through the permutations
    for perm in permutations:
        # Skip the permutation if the first and second destinations are the same or if the final destination is not the same as the start
        if perm[0] == perm[1] or perm[-1] != start:
            continue

        # Set the current distance to the distance between the start and the first destination
        curr_distance = distances[start][perm[0]]

        # Set the current path to the start
        curr_path = [start]

        # Iterate through the pairs of destinations in the permutation
        for i in range(len(perm) - 1):
            # Add the distance between the current destination and the next destination
            curr_distance += distances[perm[i]][perm[i + 1]]
            # Add the current destination to the current path
            curr_path.append(perm[i])

        # Add the distance between the last destination and the start
        curr_distance += distances[perm[-1]][start]
        # Add the last destination to the current path
        curr_path.append(perm[-1])

        # If the current distance is less than the minimum distance, update the minimum distance and the best path
        if curr_distance < min_distance:
            min_distance = curr_distance
            best_path = curr_path

    # Return the minimum distance and the best path
    return min_distance, best_path


# def is_symmetric(d):
#     """
#     This function was built to sanity-check that the distances dictionaries in the test cases below are indeed symmetric.
#     """
#     for key, value in d.items():
#         for inner_key, inner_value in value.items():
#             if key != inner_key and inner_value != d[inner_key][key]:
#                 return False
#     return True


# Test case 1: 4 nodes
distances = {
    'A': {'A': 0, 'B': 2, 'C': 3, 'D': 9},
    'B': {'A': 2, 'B': 0, 'C': 6, 'D': 5},
    'C': {'A': 3, 'B': 6, 'C': 0, 'D': 4},
    'D': {'A': 9, 'B': 5, 'C': 4, 'D': 0}
}
print(tsp_brute_force(['A', 'B', 'C', 'D'], distances, 'A'))  # Prints (14, ['A', 'B', 'D', 'C', 'A'])


# Test case 2: 4 nodes
distances = {
    'A': {'A': 0, 'B': 8, 'C': 6, 'D': 3},
    'B': {'A': 8, 'B': 0, 'C': 5, 'D': 5},
    'C': {'A': 6, 'B': 5, 'C': 0, 'D': 1},
    'D': {'A': 3, 'B': 5, 'C': 1, 'D': 0}
}
print(tsp_brute_force(['A', 'B', 'C', 'D'], distances, 'A'))  # Prints (17, ['A', 'B', 'C', 'D', 'A'])


# Test case 3: 5 nodes
distances = {
    'A': {'A': 0, 'B': 12, 'C': 3, 'D': 6, 'E': 8},
    'B': {'A': 12, 'B': 0, 'C': 4, 'D': 4, 'E': 5},
    'C': {'A': 3, 'B': 4, 'C': 0, 'D': 9, 'E': 1},
    'D': {'A': 6, 'B': 4, 'C': 9, 'D': 0, 'E': 4},
    'E': {'A': 8, 'B': 5, 'C': 1, 'D': 4, 'E': 0},
}
print(tsp_brute_force(['A', 'B', 'C', 'D', 'E'], distances, 'A'), '\n')  # Prints (19, ['A', 'C', 'E', 'B', 'D', 'A'])


# Test case 4: 10 nodes
t1 = time.time()
distances = {
    'A': {'A': 0, 'B': 12, 'C': 3, 'D': 6, 'E': 8, 'F': 7, 'G': 9, 'H': 1, 'I': 13, 'J': 8},
    'B': {'A': 12, 'B': 0, 'C': 2, 'D': 2, 'E': 9, 'F': 14, 'G': 17, 'H': 6, 'I': 3, 'J': 4},
    'C': {'A': 3, 'B': 2, 'C': 0, 'D': 1, 'E': 5, 'F': 5, 'G': 2, 'H': 4, 'I': 1, 'J': 7},
    'D': {'A': 6, 'B': 2, 'C': 1, 'D': 0, 'E': 3, 'F': 3, 'G': 10, 'H': 19, 'I': 20, 'J': 28},
    'E': {'A': 8, 'B': 9, 'C': 5, 'D': 3, 'E': 0, 'F': 4, 'G': 11, 'H': 14, 'I': 8, 'J': 1},
    'F': {'A': 7, 'B': 14, 'C': 5, 'D': 3, 'E': 4, 'F': 0, 'G': 12, 'H': 1, 'I': 1, 'J': 2},
    'G': {'A': 9, 'B': 17, 'C': 2, 'D': 10, 'E': 11, 'F': 12, 'G': 0, 'H': 13, 'I': 16, 'J': 18},
    'H': {'A': 1, 'B': 6, 'C': 4, 'D': 19, 'E': 14, 'F': 1, 'G': 13, 'H': 13, 'I': 6, 'J': 8},
    'I': {'A': 13, 'B': 3, 'C': 1, 'D': 20, 'E': 8, 'F': 1, 'G': 16, 'H': 6, 'I': 0, 'J': 2},
    'J': {'A': 8, 'B': 4, 'C': 7, 'D': 28, 'E': 1, 'F': 2, 'G': 18, 'H': 8, 'I': 2, 'J': 0}
}
print(tsp_brute_force(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'], distances, 'A'))  # Prints (24, ['A', 'G', 'C', 'B', 'D', 'E', 'J', 'I', 'F', 'H', 'A'])
t2 = time.time()
print("Computing the above output with 10 nodes took ", round(t2-t1, 3), " seconds.", '\n')


# Test case 5: 11 nodes
t1 = time.time()
distances = {
    'A': {'A': 0, 'B': 37, 'C': 85, 'D': 64, 'E': 81, 'F': 20, 'G': 63, 'H': 97, 'I': 20, 'J': 58, 'K': 91},
    'B': {'A': 37, 'B': 0, 'C': 97, 'D': 44, 'E': 17, 'F': 14, 'G': 58, 'H': 72, 'I': 54, 'J': 67, 'K': 75},
    'C': {'A': 85, 'B': 97, 'C': 0, 'D': 28, 'E': 40, 'F': 39, 'G': 51, 'H': 79, 'I': 44, 'J': 60, 'K': 11},
    'D': {'A': 64, 'B': 44, 'C': 28, 'D': 0, 'E': 39, 'F': 7, 'G': 84, 'H': 67, 'I': 8, 'J': 66, 'K': 95},
    'E': {'A': 81, 'B': 17, 'C': 40, 'D': 39, 'E': 0, 'F': 29, 'G': 44, 'H': 23, 'I': 4, 'J': 79, 'K': 71},
    'F': {'A': 20, 'B': 14, 'C': 39, 'D': 7, 'E': 29, 'F': 0, 'G': 23, 'H': 75, 'I': 65, 'J': 97, 'K': 54},
    'G': {'A': 63, 'B': 58, 'C': 51, 'D': 84, 'E': 44, 'F': 23, 'G': 0, 'H': 97, 'I': 12, 'J': 70, 'K': 96},
    'H': {'A': 97, 'B': 72, 'C': 79, 'D': 67, 'E': 23, 'F': 75, 'G': 97, 'H': 0, 'I': 25, 'J': 65, 'K': 18},
    'I': {'A': 20, 'B': 54, 'C': 44, 'D': 8, 'E': 4, 'F': 65, 'G': 12, 'H': 25, 'I': 0, 'J': 88, 'K': 56},
    'J': {'A': 58, 'B': 67, 'C': 60, 'D': 66, 'E': 79, 'F': 97, 'G': 70, 'H': 65, 'I': 88, 'J': 0, 'K': 89},
    'K': {'A': 91, 'B': 75, 'C': 11, 'D': 95, 'E': 71, 'F': 54, 'G': 96, 'H': 18, 'I': 56, 'J': 89, 'K': 0}
}
print(tsp_brute_force(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'], distances, 'A'))   # Prints (279, ['A', 'F', 'B', 'E', 'H', 'K', 'C', 'D', 'I', 'G', 'J', 'A'])
t2 = time.time()
print("Computing the above output with 11 nodes took ", round(t2-t1, 3), " seconds." )


# Test case 6: 11 nodes - same distances dictionary as Test case 5, but the order of the nodes input into the function differs. The total travel time should be the same in these two test cases (279).
t1 = time.time()
print(tsp_brute_force(['A', 'J', 'C', 'D', 'E', 'K', 'I', 'G', 'H', 'F', 'B'], distances, 'A'))  # Prints (279, ['A', 'J', 'G', 'I', 'D', 'C', 'K', 'H', 'E', 'B', 'F', 'A'])
t2 = time.time()
print("Computing the above output with 11 nodes took ", round(t2-t1, 3), " seconds." )