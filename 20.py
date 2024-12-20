from math import inf
from turtle import position
from utils import read_data


# Shared logic

WALL_CHAR = "#"
START_CHAR = "S"
END_CHAR = "E"
DESIRED_SAVING = 100

def get_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def get_neighbours(field_size, position, max_distance = 1):
    for i_shift in range(-max_distance, max_distance + 1):
        for j_shift in range(-max_distance + abs(i_shift), max_distance - abs(i_shift) + 1):
            neighbour = (position[0] + i_shift, position[1] + j_shift)
            if 0 <= neighbour[0] < field_size[0] and 0 <= neighbour[1] < field_size[1] and neighbour != position:
                yield neighbour

def get_distances_from_start(field_size, wall_positions, start_position, end_position):
    distances_from_start = {(i, j): inf for i in range(field_size[0]) for j in range(field_size[1])}
    distances_from_start[start_position] = 0
    queue = [start_position]

    while any(queue):
        position = queue.pop(0)
        if position == end_position:
            continue
        for neighbour in get_neighbours(field_size, position):
            if neighbour not in wall_positions and distances_from_start[position] + 1 < distances_from_start[neighbour]:
                distances_from_start[neighbour] = distances_from_start[position] + 1
                queue.append(neighbour)
    return {position: distance for position, distance in distances_from_start.items() if distance != inf}

def get_positions(field, char_to_find):
    return [(i, j) for i, row in enumerate(field) for j, symbol in enumerate(row) if symbol == char_to_find]

data = read_data(20)
field_size = (len(data), len(data[0]))
wall_positions = get_positions(data, WALL_CHAR)
start_position = get_positions(data, START_CHAR)[0]
end_position = get_positions(data, END_CHAR)[0]

distances_from_start = get_distances_from_start(field_size, wall_positions, start_position, end_position)


# Part 1

result = 0
for position, distance in distances_from_start.items():
    for neighbour in get_neighbours(field_size, position, 2):
        if neighbour not in distances_from_start:
          continue
        saving = distance - distances_from_start[neighbour] - get_distance(position, neighbour)
        if saving >= DESIRED_SAVING:
            result += 1

print(result)


# Part 2

cheats = set()
for position, distance in distances_from_start.items():
    for neighbour in get_neighbours(field_size, position, 20):
        if neighbour not in distances_from_start:
          continue
        saving = distance - distances_from_start[neighbour] - get_distance(position, neighbour)
        if saving >= DESIRED_SAVING:
            cheats.add((position, neighbour))

print(len(cheats))
