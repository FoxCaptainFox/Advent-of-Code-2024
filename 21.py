from functools import cache
from math import copysign
from typing import Counter
from utils import read_data


# Shared logic

NUMBERIC_KEYBOARD = (("7", "8", "9"),
                           ("4", "5", "6"),
                           ("1", "2", "3"),
                           (None, "0", "A"))

DIRECTIONAL_KEYBOARD = ((None, "^", "A"),
                              ("<", "v", ">"))

DIRECTION_CHARS = {
    (-1, 0): "^",
    (0, -1): "<",
    (1, 0): "v",
    (0, 1): ">"
}

def get_position(field, char_to_find):
    return [(i, j) for i, row in enumerate(field) for j, symbol in enumerate(row) if symbol == char_to_find][0]


# Part 1

def get_possible_directions(keyboard, code):
    previous_position = get_position(keyboard, "A")
    current_directions = [""]
    for code_char in code:
        new_directions = []
        this_position = get_position(keyboard, code_char)
        for possible_directions in get_possible_directions_from_a_to_b(previous_position, this_position, keyboard):
            new_directions += [cd + possible_directions for cd in current_directions]
        current_directions = new_directions
        previous_position = this_position
    return current_directions

def get_possible_directions_from_a_to_b(a, b, keyboard):
    queue = [[]]
    while len(queue) > 0:
        directions = queue.pop()
        i_change = sum([direction[0] for direction in directions])
        j_change = sum([direction[1] for direction in directions])
        this_position = (a[0] + i_change, a[1] + j_change)
        if keyboard[this_position[0]][this_position[1]] is None:
            continue
        if this_position == b:
            yield "".join([DIRECTION_CHARS[direction] for direction in directions]) + "A"
        if this_position[0] != b[0]:
            queue.append(directions + [(int(copysign(1, b[0] - a[0])), 0)])        
        if this_position[1] != b[1]:
            queue.append(directions + [(0, int(copysign(1, b[1] - a[1])))])

data = read_data(21)
complexity_sum = 0
for original_code in data:
    directions_1 = get_possible_directions(NUMBERIC_KEYBOARD, original_code)
    directions_2 = [direction_2 
                    for direction_1 in directions_1 
                    for direction_2 in get_possible_directions(DIRECTIONAL_KEYBOARD, direction_1)]
    directions_3 = [direction_3 
                    for direction_2 in directions_2 
                    for direction_3 in get_possible_directions(DIRECTIONAL_KEYBOARD, direction_2)]
    code_as_int = int(original_code[:-1])
    shortest_key = min(directions_3, key=len)
    complexity_sum += code_as_int * len(shortest_key)
print(complexity_sum)


# Part 2

def get_directions(keyboard, word_counter):
    result = Counter()
    for word, count in word_counter.items():
        previous_position = get_position(keyboard, "A")
        for character in word:
            this_position = get_position(keyboard, character)
            directions = get_directions_from_a_to_b(previous_position, this_position, keyboard)
            result += Counter({directions: count})
            previous_position = this_position
    return result

def get_directions_from_a_to_b(a, b, keyboard):
    i_change, j_change = b[0] - a[0], b[1] - a[1]
    i_directions = DIRECTION_CHARS[(copysign(1, i_change), 0)] * abs(i_change)
    j_directions = DIRECTION_CHARS[(0, copysign(1, j_change))] * abs(j_change)

    if keyboard[b[0]][a[1]] is None:
        return j_directions + i_directions + "A"
    if keyboard[a[0]][b[1]] is None:
        return i_directions + j_directions + "A"
    
    # Prioritize left movement, then vertical, then right
    # Found heuristically that farther movement buttons should be pressed first
    if j_change < 0:
        return j_directions + i_directions + "A"
    return i_directions + j_directions + "A"


DIRECTIONAL_KEYBOARDS_NUMBER = 25

data = read_data(21)
complexity_sum = 0
for original_code in data:
    directions = get_directions(NUMBERIC_KEYBOARD, Counter({original_code: 1}))
    for i in range(DIRECTIONAL_KEYBOARDS_NUMBER):
        directions = get_directions(DIRECTIONAL_KEYBOARD, directions)
    directions_length = sum([len(value) * count for value, count in directions.items()])
    code_as_int = int(original_code[:-1])
    complexity_sum += code_as_int * directions_length
print(complexity_sum)
