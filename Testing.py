from TSP_Christofides import christofides_algorithm

# Test case 1: 3 nodes
# G1 = [("A", "B", 6), ("A", "C", 3), ("B", "C", 4)]
# print("Test case 1:", christofides_algorithm(G1, "A"), "\n")

# Test case 2: 4 nodes
# G2 = [("A", "B", 8), ("A", "C", 12), ("A", "D", 9),
#       ("B", "C", 6), ("B", "D", 9),
#       ("C", "D", 7)]
# print("Test case 2:", christofides_algorithm(G2, "A"), "\n")

# Test case 3: 5 nodes
G3 = [("A", "B", 18), ("A", "C", 11), ("A", "D", 16), ("A", "E", 11),
      ("B", "C", 9), ("B", "D", 15), ("B", "E", 11),
      ("C", "D", 12), ("C", "E", 14),
      ("D", "E", 12)]
print("Test case 3:", christofides_algorithm(G3, "A"), "\n")


# Test case 4: 6 nodes
G4 = [("A", "B", ), ("A", "C", ), ("A", "D", ), ("A", "E", ), ("A", "F", ),
      ("B", "C", ), ("B", "D", ), ("B", "E", ), ("B", "F", ),
      ("C", "D", ), ("C", "E", ), ("C", "F", ),
      ("D", "E", ), ("D", "F", ),
      ("E", "F", )]

#Test case 5: 10 nodes
G5 = [("A", "B", ), ("A", "C", ), ("A", "D", ), ("A", "E", ), ("A", "F", ), ("A", "G", ), ("A", "H", ), ("A", "I", ), ("A", "J", ),
      ("B", "C", ), ("B", "D", ), ("B", "E", ), ("B", "F", ), ("B", "G", ), ("B", "H", ), ("B", "I", ), ("B", "J", ),
      ("C", "D", ), ("C", "E", ), ("C", "F", ), ("C", "G", ), ("C", "H", ), ("C", "I", ), ("C", "J", ),
      ("D", "E", ), ("D", "F", ), ("D", "G", ), ("D", "H", ), ("D", "I", ), ("D", "J", ),
      ("E", "F", ), ("E", "G", ), ("E", "H", ), ("E", "I", ), ("E", "J", ),
      ("F", "G", ), ("F", "H", ), ("F", "I", ), ("F", "J", ),
      ("G", "H", ), ("G", "I", ), ("G", "J", ),
      ("H", "I", ), ("H", "J", ),
      ("I", "J", )]

#Test case 6: 11 nodes
G6 = [("A", "B", ), ("A", "C", ), ("A", "D", ), ("A", "E", ), ("A", "F", ), ("A", "G", ), ("A", "H", ), ("A", "I", ), ("A", "J", ), ("A", "K", ),
      ("B", "C", ), ("B", "D", ), ("B", "E", ), ("B", "F", ), ("B", "G", ), ("B", "H", ), ("B", "I", ), ("B", "J", ), ("B", "K", ),
      ("C", "D", ), ("C", "E", ), ("C", "F", ), ("C", "G", ), ("C", "H", ), ("C", "I", ), ("C", "J", ), ("C", "K", ),
      ("D", "E", ), ("D", "F", ), ("D", "G", ), ("D", "H", ), ("D", "I", ), ("D", "J", ), ("D", "K", ),
      ("E", "F", ), ("E", "G", ), ("E", "H", ), ("E", "I", ), ("E", "J", ), ("E", "K", ),
      ("F", "G", ), ("F", "H", ), ("F", "I", ), ("F", "J", ), ("F", "K", ),
      ("G", "H", ), ("G", "I", ), ("G", "J", ), ("G", "K", ),
      ("H", "I", ), ("H", "J", ), ("H", "K", ),
      ("I", "J", ), ("I", "K", ),
      ("J", "K", )]

