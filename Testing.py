from TSP_Brute_Force import tsp_brute_force
from TSP_Greedy import tsp_greedy
from TSP_Christofides import tsp_christofides
import time


# Test case: 4 nodes
G = {
    'A': {'A': 0, 'B': 2, 'C': 3, 'D': 9},
    'B': {'A': 2, 'B': 0, 'C': 6, 'D': 5},
    'C': {'A': 3, 'B': 6, 'C': 0, 'D': 4},
    'D': {'A': 9, 'B': 5, 'C': 4, 'D': 0}
}
start = 'A'

t1_brute_force = time.time()
brute_force_cycle = tsp_brute_force(G, start)
t2_brute_force = time.time()

t1_greedy = time.time()
greedy_cycle = tsp_greedy(G, start)
t2_greedy = time.time()

t1_christofides = time.time()
christofides_cycle = tsp_christofides(G, start)
t2_christofides = time.time()

print('Test case: 4 nodes')
print('Brute force:  ', tsp_brute_force(G, start))  # Prints (14, [('A', 'B', 2), ('B', 'D', 5), ('D', 'C', 4), ('C', 'A', 3)])
print('Greedy:       ', tsp_greedy(G, start))
print('Christofides: ', tsp_christofides(G, start))
print('Time (Brute force):',  round(t2_brute_force - t1_brute_force, 3), 'seconds,   ',
      'Time (Greedy):',       round(t2_greedy - t1_greedy, 3), 'seconds,   ',
      'Time (Christofides):', round(t2_christofides - t1_christofides, 3), 'seconds', '\n')


# Test case: 4 nodes
G = {
    'A': {'A': 0, 'B': 9, 'C': 6, 'D': 8},
    'B': {'A': 9, 'B': 0, 'C': 3, 'D': 2},
    'C': {'A': 6, 'B': 3, 'C': 0, 'D': 5},
    'D': {'A': 8, 'B': 2, 'C': 5, 'D': 0}
}
start = 'A'

t1_brute_force = time.time()
brute_force_cycle = tsp_brute_force(G, start)
t2_brute_force = time.time()

t1_greedy = time.time()
greedy_cycle = tsp_greedy(G, start)
t2_greedy = time.time()

t1_christofides = time.time()
christofides_cycle = tsp_christofides(G, start)
t2_christofides = time.time()

print('Test case: 4 nodes')
print('Brute force:  ', tsp_brute_force(G, start))
print('Greedy:       ', tsp_greedy(G, start))
print('Christofides: ', tsp_christofides(G, start))  # Prints (19, [('A', 'D', 8), ('D', 'B', 2), ('B', 'C', 3), ('C', 'A', 6)])
print('Time (Brute force):',  round(t2_brute_force - t1_brute_force, 3), 'seconds,   ',
      'Time (Greedy):',       round(t2_greedy - t1_greedy, 3), 'seconds,   ',
      'Time (Christofides):', round(t2_christofides - t1_christofides, 3), 'seconds', '\n')


# Test case: 4 nodes
G = {
    'A': {'A': 0, 'B': 8, 'C': 6, 'D': 3},
    'B': {'A': 8, 'B': 0, 'C': 5, 'D': 5},
    'C': {'A': 6, 'B': 5, 'C': 0, 'D': 1},
    'D': {'A': 3, 'B': 5, 'C': 1, 'D': 0}
}
start = 'A'

t1_brute_force = time.time()
brute_force_cycle = tsp_brute_force(G, start)
t2_brute_force = time.time()

t1_greedy = time.time()
greedy_cycle = tsp_greedy(G, start)
t2_greedy = time.time()

t1_christofides = time.time()
christofides_cycle = tsp_christofides(G, start)
t2_christofides = time.time()

print('Test case: 4 nodes')
print('Brute force:  ', tsp_brute_force(G, start))  # Prints (17, [('A', 'B', 8), ('B', 'C', 5), ('C', 'D', 1), ('D', 'A', 3)])
print('Greedy:       ', tsp_greedy(G, start))
print('Christofides: ', tsp_christofides(G, start))
print('Time (Brute force):',  round(t2_brute_force - t1_brute_force, 3), 'seconds,   ',
      'Time (Greedy):',       round(t2_greedy - t1_greedy, 3), 'seconds,   ',
      'Time (Christofides):', round(t2_christofides - t1_christofides, 3), 'seconds', '\n')


# Test case: 4 nodes
G = {
    'A': {'A': 0, 'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'B': 0, 'C': 4, 'D': 6},
    'C': {'A': 3, 'B': 4, 'C': 0, 'D': 5},
    'D': {'A': 1, 'B': 6, 'C': 5, 'D': 0}
}
start = 'A'

t1_brute_force = time.time()
brute_force_cycle = tsp_brute_force(G, start)
t2_brute_force = time.time()

t1_greedy = time.time()
greedy_cycle = tsp_greedy(G, start)
t2_greedy = time.time()

t1_christofides = time.time()
christofides_cycle = tsp_christofides(G, start)
t2_christofides = time.time()

print('Test case: 4 nodes')
print('Brute force:  ', tsp_brute_force(G, start))
print('Greedy:       ', tsp_greedy(G, start))
print('Christofides: ', tsp_christofides(G, start))
print('Time (Brute force):',  round(t2_brute_force - t1_brute_force, 3), 'seconds,   ',
      'Time (Greedy):',       round(t2_greedy - t1_greedy, 3), 'seconds,   ',
      'Time (Christofides):', round(t2_christofides - t1_christofides, 3), 'seconds', '\n')


# Test case: 5 nodes
G = {
    'A': {'A': 0, 'B': 2, 'C': 4, 'D': 1, 'E': 3},
    'B': {'A': 2, 'B': 0, 'C': 1, 'D': 3, 'E': 4},
    'C': {'A': 4, 'B': 1, 'C': 0, 'D': 2, 'E': 5},
    'D': {'A': 1, 'B': 3, 'C': 2, 'D': 0, 'E': 6},
    'E': {'A': 3, 'B': 4, 'C': 5, 'D': 6, 'E': 0}
}
start = 'A'

t1_brute_force = time.time()
brute_force_cycle = tsp_brute_force(G, start)
t2_brute_force = time.time()

t1_greedy = time.time()
greedy_cycle = tsp_greedy(G, start)
t2_greedy = time.time()

t1_christofides = time.time()
christofides_cycle = tsp_christofides(G, start)
t2_christofides = time.time()

print('Test case: 5 nodes')
print('Brute force:  ', tsp_brute_force(G, start))
print('Greedy:       ', tsp_greedy(G, start))
print('Christofides: ', tsp_christofides(G, start))
print('Time (Brute force):',  round(t2_brute_force - t1_brute_force, 3), 'seconds,   ',
      'Time (Greedy):',       round(t2_greedy - t1_greedy, 3), 'seconds,   ',
      'Time (Christofides):', round(t2_christofides - t1_christofides, 3), 'seconds', '\n')


# Test case: 5 nodes
G = {
    'A': {'A': 0, 'B': 10, 'C': 20, 'D': 30, 'E': 40},
    'B': {'A': 10, 'B': 0, 'C': 15, 'D': 25, 'E': 35},
    'C': {'A': 20, 'B': 15, 'C': 0, 'D': 5, 'E': 15},
    'D': {'A': 30, 'B': 25, 'C': 5, 'D': 0, 'E': 10},
    'E': {'A': 40, 'B': 35, 'C': 15, 'D': 10, 'E': 0}
}
start = 'A'

t1_brute_force = time.time()
brute_force_cycle = tsp_brute_force(G, start)
t2_brute_force = time.time()

t1_greedy = time.time()
greedy_cycle = tsp_greedy(G, start)
t2_greedy = time.time()

t1_christofides = time.time()
christofides_cycle = tsp_christofides(G, start)
t2_christofides = time.time()

print('Test case: 5 nodes')
print('Brute force:  ', tsp_brute_force(G, start))
print('Greedy:       ', tsp_greedy(G, start))
print('Christofides: ', tsp_christofides(G, start))  # Prints (80, [('A', 'E', 40), ('E', 'D', 10), ('D', 'C', 5), ('C', 'B', 15), ('B', 'A', 10)])
print('Time (Brute force):',  round(t2_brute_force - t1_brute_force, 3), 'seconds,   ',
      'Time (Greedy):',       round(t2_greedy - t1_greedy, 3), 'seconds,   ',
      'Time (Christofides):', round(t2_christofides - t1_christofides, 3), 'seconds', '\n')


# Test case: 5 nodes
G = {
    'A': {'A': 0, 'B': 12, 'C': 3, 'D': 6, 'E': 8},
    'B': {'A': 12, 'B': 0, 'C': 4, 'D': 4, 'E': 5},
    'C': {'A': 3, 'B': 4, 'C': 0, 'D': 9, 'E': 1},
    'D': {'A': 6, 'B': 4, 'C': 9, 'D': 0, 'E': 4},
    'E': {'A': 8, 'B': 5, 'C': 1, 'D': 4, 'E': 0},
}
start = 'A'

t1_brute_force = time.time()
brute_force_cycle = tsp_brute_force(G, start)
t2_brute_force = time.time()

t1_greedy = time.time()
greedy_cycle = tsp_greedy(G, start)
t2_greedy = time.time()

t1_christofides = time.time()
christofides_cycle = tsp_christofides(G, start)
t2_christofides = time.time()

print('Test case: 5 nodes')
print('Brute force:  ', tsp_brute_force(G, start))  # Prints (19, [('A', 'C', 3), ('C', 'E', 1), ('E', 'B', 5), ('B', 'D', 4), ('D', 'A', 6)])
print('Greedy:       ', tsp_greedy(G, start))
print('Christofides: ', tsp_christofides(G, start))
print('Time (Brute force):',  round(t2_brute_force - t1_brute_force, 3), 'seconds,   ',
      'Time (Greedy):',       round(t2_greedy - t1_greedy, 3), 'seconds,   ',
      'Time (Christofides):', round(t2_christofides - t1_christofides, 3), 'seconds', '\n')


# Test case: 6 nodes
G = {
    'A': {'A': 0, 'B': 3, 'C': 1, 'D': 2, 'E': 5, 'F': 4},
    'B': {'A': 3, 'B': 0, 'C': 4, 'D': 6, 'E': 2, 'F': 3},
    'C': {'A': 1, 'B': 4, 'C': 0, 'D': 3, 'E': 4, 'F': 2},
    'D': {'A': 2, 'B': 6, 'C': 3, 'D': 0, 'E': 1, 'F': 5},
    'E': {'A': 5, 'B': 2, 'C': 4, 'D': 1, 'E': 0, 'F': 6},
    'F': {'A': 4, 'B': 3, 'C': 2, 'D': 5, 'E': 6, 'F': 0}
}
start = 'A'

t1_brute_force = time.time()
brute_force_cycle = tsp_brute_force(G, start)
t2_brute_force = time.time()

t1_greedy = time.time()
greedy_cycle = tsp_greedy(G, start)
t2_greedy = time.time()

t1_christofides = time.time()
christofides_cycle = tsp_christofides(G, start)
t2_christofides = time.time()

print('Test case: 6 nodes')
print('Brute force:  ', tsp_brute_force(G, start))
print('Greedy:       ', tsp_greedy(G, start))
print('Christofides: ', tsp_christofides(G, start))
print('Time (Brute force):',  round(t2_brute_force - t1_brute_force, 3), 'seconds,   ',
      'Time (Greedy):',       round(t2_greedy - t1_greedy, 3), 'seconds,   ',
      'Time (Christofides):', round(t2_christofides - t1_christofides, 3), 'seconds', '\n')


# Test case: 7 nodes
G = {
    'A': {'A': 0, 'B': 4, 'C': 1, 'D': 3, 'E': 7, 'F': 5, 'G': 6},
    'B': {'A': 4, 'B': 0, 'C': 6, 'D': 5, 'E': 3, 'F': 2, 'G': 7},
    'C': {'A': 1, 'B': 6, 'C': 0, 'D': 4, 'E': 2, 'F': 7, 'G': 3},
    'D': {'A': 3, 'B': 5, 'C': 4, 'D': 0, 'E': 6, 'F': 1, 'G': 2},
    'E': {'A': 7, 'B': 3, 'C': 2, 'D': 6, 'E': 0, 'F': 4, 'G': 5},
    'F': {'A': 5, 'B': 2, 'C': 7, 'D': 1, 'E': 4, 'F': 0, 'G': 6},
    'G': {'A': 6, 'B': 7, 'C': 3, 'D': 2, 'E': 5, 'F': 6, 'G': 0}
}
start = 'A'

t1_brute_force = time.time()
brute_force_cycle = tsp_brute_force(G, start)
t2_brute_force = time.time()

t1_greedy = time.time()
greedy_cycle = tsp_greedy(G, start)
t2_greedy = time.time()

t1_christofides = time.time()
christofides_cycle = tsp_christofides(G, start)
t2_christofides = time.time()

print('Test case: 7 nodes')
print('Brute force:  ', tsp_brute_force(G, start))
print('Greedy:       ', tsp_greedy(G, start))
print('Christofides: ', tsp_christofides(G, start))
print('Time (Brute force):',  round(t2_brute_force - t1_brute_force, 3), 'seconds,   ',
      'Time (Greedy):',       round(t2_greedy - t1_greedy, 3), 'seconds,   ',
      'Time (Christofides):', round(t2_christofides - t1_christofides, 3), 'seconds', '\n')


# Test case: 8 nodes
G = {
    'A': {'A': 0, 'B': 5, 'C': 2, 'D': 4, 'E': 8, 'F': 7, 'G': 3, 'H': 1},
    'B': {'A': 5, 'B': 0, 'C': 3, 'D': 7, 'E': 5, 'F': 6, 'G': 4, 'H': 2},
    'C': {'A': 2, 'B': 3, 'C': 0, 'D': 6, 'E': 4, 'F': 5, 'G': 7, 'H': 8},
    'D': {'A': 4, 'B': 7, 'C': 6, 'D': 0, 'E': 3, 'F': 2, 'G': 1, 'H': 5},
    'E': {'A': 8, 'B': 5, 'C': 4, 'D': 3, 'E': 0, 'F': 1, 'G': 6, 'H': 7},
    'F': {'A': 7, 'B': 6, 'C': 5, 'D': 2, 'E': 1, 'F': 0, 'G': 8, 'H': 3},
    'G': {'A': 3, 'B': 4, 'C': 7, 'D': 1, 'E': 6, 'F': 8, 'G': 0, 'H': 4},
    'H': {'A': 1, 'B': 2, 'C': 8, 'D': 5, 'E': 7, 'F': 3, 'G': 4, 'H': 0}
}
start = 'A'

t1_brute_force = time.time()
brute_force_cycle = tsp_brute_force(G, start)
t2_brute_force = time.time()

t1_greedy = time.time()
greedy_cycle = tsp_greedy(G, start)
t2_greedy = time.time()

t1_christofides = time.time()
christofides_cycle = tsp_christofides(G, start)
t2_christofides = time.time()

print('Test case: 8 nodes')
print('Brute force:  ', tsp_brute_force(G, start))
print('Greedy:       ', tsp_greedy(G, start))
print('Christofides: ', tsp_christofides(G, start))
print('Time (Brute force):',  round(t2_brute_force - t1_brute_force, 3), 'seconds,   ',
      'Time (Greedy):',       round(t2_greedy - t1_greedy, 3), 'seconds,   ',
      'Time (Christofides):', round(t2_christofides - t1_christofides, 3), 'seconds', '\n')


# Test case: 10 nodes
G = {
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
start = 'A'

t1_brute_force = time.time()
brute_force_cycle = tsp_brute_force(G, start)
t2_brute_force = time.time()

t1_greedy = time.time()
greedy_cycle = tsp_greedy(G, start)
t2_greedy = time.time()

t1_christofides = time.time()
christofides_cycle = tsp_christofides(G, start)
t2_christofides = time.time()

print('Test case: 10 nodes')
print('Brute force:  ', tsp_brute_force(G, start))  # Prints (24, [('A', 'G', 9), ('G', 'C', 2), ('C', 'B', 2), ('B', 'D', 2), ('D', 'E', 3), ('E', 'J', 1), ('J', 'I', 2), ('I', 'F', 1), ('F', 'H', 1), ('H', 'A', 1)])
print('Greedy:       ', tsp_greedy(G, start))
print('Christofides: ', tsp_christofides(G, start))
print('Time (Brute force):',  round(t2_brute_force - t1_brute_force, 3), 'seconds,   ',
      'Time (Greedy):',       round(t2_greedy - t1_greedy, 3), 'seconds,   ',
      'Time (Christofides):', round(t2_christofides - t1_christofides, 3), 'seconds', '\n')


# Test case: 11 nodes
G = {
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
start = 'A'

t1_brute_force = time.time()
brute_force_cycle = tsp_brute_force(G, start)
t2_brute_force = time.time()

t1_greedy = time.time()
greedy_cycle = tsp_greedy(G, start)
t2_greedy = time.time()

t1_christofides = time.time()
christofides_cycle = tsp_christofides(G, start)
t2_christofides = time.time()

print('Test case: 11 nodes')
print('Brute force:  ', tsp_brute_force(G, start))   # Prints (279, [('A', 'F', 20), ('F', 'B', 14), ('B', 'E', 17), ('E', 'H', 23), ('H', 'K', 18), ('K', 'C', 11), ('C', 'D', 28), ('D', 'I', 8), ('I', 'G', 12), ('G', 'J', 70), ('J', 'A', 58)])
print('Greedy:       ', tsp_greedy(G, start))
print('Christofides: ', tsp_christofides(G, start))
print('Time (Brute force):',  round(t2_brute_force - t1_brute_force, 3), 'seconds,   ',
      'Time (Greedy):',       round(t2_greedy - t1_greedy, 3), 'seconds,   ',
      'Time (Christofides):', round(t2_christofides - t1_christofides, 3), 'seconds', '\n')









































































































































































































































































































































































































































































































































































































































































































































































































G = {
    'A': {'A': 0, 'B': 8, 'C': 6, 'D': 3},
    'B': {'A': 8, 'B': 0, 'C': 5, 'D': 5},
    'C': {'A': 6, 'B': 5, 'C': 0, 'D': 1},
    'D': {'A': 3, 'B': 5, 'C': 1, 'D': 0}
}

G = {
    'A': {'B': 2, 'C': 3, 'D': 1},
    'B': {'A': 2, 'C': 4, 'D': 6},
    'C': {'A': 3, 'B': 4, 'D': 5},
    'D': {'A': 1, 'B': 6, 'C': 5}
}


G = {
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