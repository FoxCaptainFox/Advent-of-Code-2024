from math import inf, isinf
from utils import read_data


# Shared logic

FIELD_SIZE = (71, 71)

def get_neighbours(position):
    i, j = position
    if 0 <= i - 1:
        yield (i - 1, j)
    if i + 1 < FIELD_SIZE[0]:
        yield (i + 1, j)
    if 0 <= j - 1:
        yield (i, j - 1)
    if j + 1 < FIELD_SIZE[1]:
        yield (i, j + 1)


def get_shortest_path(obstacles):
    distances_from_start = {(i, j): inf for i in range(FIELD_SIZE[0]) for j in range(FIELD_SIZE[1])}

    start_position = (0, 0)
    end_position = (FIELD_SIZE[0] - 1, FIELD_SIZE[1] - 1)
    distances_from_start[start_position] = 0

    queue = [start_position]

    while any(queue):
        new_queue = []
        for position in queue:
            if distances_from_start[end_position] <= distances_from_start[position]:
                continue
            for neighbour in get_neighbours(position):
                if neighbour not in obstacles and distances_from_start[position] + 1 < distances_from_start[neighbour]:
                    distances_from_start[neighbour] = distances_from_start[position] + 1
                    new_queue.append(neighbour)
        queue = new_queue
    return distances_from_start[end_position]


# Shared data processing

data = read_data(18)
all_obstacles = [tuple(int(x) for x in line.split(",")) for line in data]


# Part 1

OBSTACLE_NUMBER_TO_TAKE = 1024

shortest_path = get_shortest_path(all_obstacles[:OBSTACLE_NUMBER_TO_TAKE])
print(shortest_path)


# Part 2

for obstacle_number in range(len(all_obstacles)):
    shortest_path = get_shortest_path(all_obstacles[:obstacle_number])
    if isinf(shortest_path):
        print(all_obstacles[obstacle_number - 1])
        break
