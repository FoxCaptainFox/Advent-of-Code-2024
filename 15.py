from utils import read_data


# Shared logic

ROBOT_SYMBOL = "@"
BOX_SYMBOL = "O"
WALL_SYMBOL = "#"
DIRECTIONS = {
    "^": (-1, 0),
    "v": (1, 0),
    "<": (0, -1),
    ">": (0, 1)
}

def add_direction_to_position(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])

def get_positions(field, symbol_to_find, func_for_positions = lambda ij: (ij[0], ij[1])):
    return [func_for_positions((i, j)) for i, row in enumerate(field) for j, symbol in enumerate(row) if symbol == symbol_to_find]


# Shared data processing

data = read_data(15)
separator_index = data.index("")
field = data[ : separator_index]
moves = "".join(data[separator_index : ])


# Part 1

robot_position = get_positions(field, ROBOT_SYMBOL)[0]
box_positions = get_positions(field, BOX_SYMBOL)
wall_positions = get_positions(field, WALL_SYMBOL)

for move in moves:
    direction = DIRECTIONS[move]
    box_positions_to_move = []
    position_to_check = add_direction_to_position(robot_position, direction)

    while position_to_check in box_positions:
        box_positions_to_move.append(position_to_check)
        position_to_check = add_direction_to_position(position_to_check, direction)

    if position_to_check in wall_positions:
        continue
    for box_index, box_position in enumerate(box_positions):
        if box_position in box_positions_to_move:
            box_positions[box_index] = add_direction_to_position(box_position, direction)
    robot_position = add_direction_to_position(robot_position, direction)

gps_coordinates = [i * 100 + j for (i, j) in box_positions]
print(sum(gps_coordinates))


# Part 2

robot_position = get_positions(field, ROBOT_SYMBOL, lambda ij: (ij[0], ij[1] * 2))[0]
box_position_pairs = get_positions(field, BOX_SYMBOL,  lambda ij: [(ij[0], ij[1] * 2), (ij[0], ij[1] * 2 + 1)])
wall_position_pairs = get_positions(field, WALL_SYMBOL, lambda ij: [(ij[0], ij[1] * 2), (ij[0], ij[1] * 2 + 1)])
wall_positions = [position for position_pair in wall_position_pairs for position in position_pair]

for move in moves:
    direction = DIRECTIONS[move]
    box_indexes_to_move = set()
    positions_to_check = set([add_direction_to_position(robot_position, direction)])
    wall_encountered = False

    while any(positions_to_check):
        if any(position_to_check in wall_positions for position_to_check in positions_to_check):
            wall_encountered = True
            break
        
        new_positions_to_check = set()
        for position_to_check in positions_to_check:
            for box_index, box_position_pair in enumerate(box_position_pairs):
                if position_to_check in box_position_pair:
                    box_indexes_to_move.add(box_index)
                    new_positions_to_check.update([
                        add_direction_to_position(box_position, direction)
                        for box_position in box_position_pair])
        positions_to_check = new_positions_to_check - positions_to_check

    if wall_encountered:
        continue

    for box_index, box_position_pair in enumerate(box_position_pairs):
        if box_index in box_indexes_to_move:
            box_position_pairs[box_index] = [
                add_direction_to_position(box_position, direction)
                for box_position in box_position_pair]
    robot_position = add_direction_to_position(robot_position, direction)

gps_coordinates = [
    min([box_position[0] for box_position in box_position_pair]) * 100 + 
    min([box_position[1] for box_position in box_position_pair]) 
    for box_position_pair in box_position_pairs
]
print(sum(gps_coordinates))
