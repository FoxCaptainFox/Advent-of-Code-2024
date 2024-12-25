from functools import cache
from itertools import combinations
from utils import read_data


# Shared logic

@cache
def get_connected_computers(computer, all_connections):
    result = []
    for connection in all_connections:
        if computer in connection:
            result.append(list(connection - set([computer]))[0])
    return set(result)


# Shared data processing

data = read_data(23)
all_connections = tuple(frozenset(line.split("-")) for line in data)
computers = frozenset.union(*all_connections)

# Part 1

possible_sets = set()
for computer in computers:
    if not computer.startswith("t"):
        continue
    neighbour_computers = get_connected_computers(computer, all_connections)
    for connected_computer_pair in combinations(neighbour_computers, 2):
        if set(connected_computer_pair) in all_connections:
            possible_sets.add(frozenset(list(connected_computer_pair) + [computer]))
print(len(possible_sets))


# Part 2

def get_common_neighbours_for_group(group, all_connections):
    return set.intersection(*list(get_connected_computers(computer, all_connections) | set([computer]) for computer in group))

found = False
for computer in computers:
    neighbour_computers = get_connected_computers(computer, all_connections)
    for neighbour in neighbour_computers:
        set_to_check = (neighbour_computers | set([computer])) - set([neighbour])
        if set_to_check == get_common_neighbours_for_group(set_to_check, all_connections):
            print(",".join(sorted(set_to_check)))
            found = True
            break
    if found:
        break
