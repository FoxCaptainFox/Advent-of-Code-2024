from math import inf
from utils import read_data


# Shared logic

WALL_CHAR = "#"
START_CHAR = "S"
END_CHAR = "E"
STEP_PRICE = 1
TURN_PRICE = 1000

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def get_positions(field, char_to_find):
    return [(i, j) for i, row in enumerate(field) for j, symbol in enumerate(row) if symbol == char_to_find]

def move_from_position(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])


# Shared data processing

data = read_data(16)
wall_positions = get_positions(data, WALL_CHAR)
start_position = get_positions(data, START_CHAR)[0]
end_position = get_positions(data, END_CHAR)[0]


# Part 1

pairs_to_check = [(start_position, 0)]
scores = {(start_position, 0): 0}
min_end_score = inf

while any(pairs_to_check):
    new_pairs_to_check = []
    for (old_position, old_direction_index) in pairs_to_check:

        old_score = scores[(old_position, old_direction_index)]
        if old_position == end_position:
            min_end_score = min(min_end_score, old_score)
            continue

        for direction_index_shift in [-1, 0, 1]:
            direction_index = (old_direction_index + direction_index_shift) % len(DIRECTIONS)
            direction = DIRECTIONS[direction_index]
            turn_number = abs(direction_index_shift)
            position = move_from_position(old_position, direction)

            if position not in wall_positions:
                score = old_score + STEP_PRICE + turn_number * TURN_PRICE
                if (position, direction_index) not in scores or score < scores[(position, direction_index)]:
                    scores[(position, direction_index)] = score
                    new_pairs_to_check.append((position, direction_index))
    pairs_to_check = new_pairs_to_check

print(min_end_score)


# Part 2

pairs_to_check = [(start_position, 0)]
scores_and_path = {(start_position, 0): (0, set([start_position]))}
min_end_score = inf
positions_in_path_to_end = set()

while any(pairs_to_check):
    new_pairs_to_check = []
    for (old_position, old_direction_index) in pairs_to_check:
        old_score, old_path = scores_and_path[(old_position, old_direction_index)]

        if old_position == end_position:
            if old_score < min_end_score:
                min_end_score = old_score
                positions_in_path_to_end = old_path
            elif old_score == min_end_score:
                positions_in_path_to_end = positions_in_path_to_end | old_path 
            continue

        for direction_index_shift in [-1, 0, 1]:
            direction_index = (old_direction_index + direction_index_shift) % len(DIRECTIONS)
            direction = DIRECTIONS[direction_index]
            turn_number = abs(direction_index_shift)
            position = move_from_position(old_position, direction)

            if position not in wall_positions:
                score = old_score + STEP_PRICE + turn_number * TURN_PRICE
                if (position, direction_index) not in scores_and_path or score < scores_and_path[(position, direction_index)][0]:
                    scores_and_path[(position, direction_index)] = score, old_path | set([position])
                    new_pairs_to_check.append((position, direction_index))
                elif score == scores_and_path[(position, direction_index)][0]:
                    scores_and_path[(position, direction_index)] = score, scores_and_path[(position, direction_index)][1] | old_path | set([position])
                    new_pairs_to_check.append((position, direction_index))

    pairs_to_check = new_pairs_to_check

print(len(positions_in_path_to_end))
