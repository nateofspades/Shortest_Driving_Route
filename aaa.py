# Want to convert  from this form...

distances = {
    'D': {'A': 9, 'B': 5, 'C': 4, 'D': 0},
    'A': {'A': 0, 'B': 2, 'C': 3, 'D': 9},
    'C': {'A': 3, 'B': 6, 'C': 0, 'D': 4},
    'B': {'A': 2, 'B': 0, 'C': 6, 'D': 5}
}


# ... to this form

distances = [("A", "B", 2), ("A", "C", 3), ("A", "D", 9),
             ("B", "C", 6), ("B", "D", 5),
             ("C", "D", 4)]


def input_converter(d):
    return

# L = []
# n = len(L)
# nodes = list(distances.keys())
# nodes.sort()
# print(nodes)
# for i in range(n):
#     for j

def convert_dict_to_list(dictionary):
  result = []
  for key1, value1 in dictionary.items():
    for key2, value2 in value1.items():
      if key1 < key2:
        result.append((key1, key2, value2))
  return result

distances = {
    'D': {'A': 9, 'B': 5, 'C': 4, 'D': 0},
    'A': {'A': 0, 'B': 2, 'C': 3, 'D': 9},
    'C': {'A': 3, 'B': 6, 'C': 0, 'D': 4},
    'B': {'A': 2, 'B': 0, 'C': 6, 'D': 5}
}
print(convert_dict_to_list(distances))

distances = {
    'A': {'A': 0, 'B': 2, 'C': 3, 'D': 9},
    'B': {'A': 2, 'B': 0, 'C': 6, 'D': 5},
    'C': {'A': 3, 'B': 6, 'C': 0, 'D': 4},
    'D': {'A': 9, 'B': 5, 'C': 4, 'D': 0}
}
print(convert_dict_to_list(distances))

for key, value in distances.items():
    print(key, value)