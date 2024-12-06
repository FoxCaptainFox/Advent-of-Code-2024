from utils import read_data


# Shared input processing

data = read_data(6)
initial_guard_position = [(ix,iy) for ix, row in enumerate(data) for iy, elem in enumerate(row) if elem == "^"][0]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]


# Part 1

direction_index = 0
guard_position = initial_guard_position
visited_locations = {guard_position}

while True:
    direction = directions[direction_index]
    next_guard_position = (guard_position[0] + direction[0], guard_position[1] + direction[1])
    if not(0 <= next_guard_position[0] < len(data) and 0 <= next_guard_position[1] < len(data[0])):
        break
    if data[next_guard_position[0]][next_guard_position[1]] == "#":
        direction_index = (direction_index + 1) % len(directions)
    else:
        guard_position = next_guard_position
        visited_locations.add(guard_position)

print(len(visited_locations))


# Part 2

def will_guard_be_looped(data, guard_position):
    visited_locations_with_direction = set()
    direction_index = 0

    while True:
        direction = directions[direction_index]
        if (guard_position, direction) in visited_locations_with_direction:
            return True
        visited_locations_with_direction.add((guard_position, direction))

        next_guard_position = (guard_position[0] + direction[0], guard_position[1] + direction[1])
        if not(0 <= next_guard_position[0] < len(data) and 0 <= next_guard_position[1] < len(data[0])):
            return False
        if data[next_guard_position[0]][next_guard_position[1]] == "#":
            direction_index = (direction_index + 1) % len(directions)
        else:
            guard_position = next_guard_position

result = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] != ".":
            continue
        modified_data = [row for row in data]
        modified_data[i] = modified_data[i][:j] + "#" + modified_data[i][j + 1:]
        if will_guard_be_looped(modified_data, initial_guard_position):
            result += 1
print(result)
