from utils import read_data

# Part 1 

SEARCH_PATTERN_1 = "XMAS"

def get_match_number(data, i, j):
    match_number = 0

    directions = [(i_direction, j_direction) 
                  for j_direction in [-1, 0, 1] 
                  for i_direction in [-1, 0, 1] 
                  if i_direction != 0 or j_direction != 0]
    
    for (i_direction, j_direction) in directions:
        pattern_is_ok = True

        for search_pattern_index in range(len(SEARCH_PATTERN_1)):
            new_i = i + search_pattern_index * i_direction
            new_j = j + search_pattern_index * j_direction

            if not(0 <= new_i < len(data) and 0 <= new_j < len(data[0])) or \
                data[new_i][new_j] != SEARCH_PATTERN_1[search_pattern_index]:
                pattern_is_ok = False
                break
        if pattern_is_ok:
            match_number += 1
    return match_number

data = read_data(4)

search_occurences = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        search_occurences += get_match_number(data, i, j)

print(search_occurences)


# Part 2

SEARCH_PATTERN_2 = "MAS"

def check_for_match(data, i, j):
    if not(0 < i < len(data) - 1 and 0 < j < len(data[0]) - 1):
        return False
    
    diagonal_from_top_left = "".join([data[i - 1][j - 1], data[i][j], data[i + 1][j + 1]])
    diagonal_from_top_right = "".join([data[i - 1][j + 1], data[i][j], data[i + 1][j - 1]])

    return (diagonal_from_top_left == SEARCH_PATTERN_2 or diagonal_from_top_left == SEARCH_PATTERN_2[::-1]) and \
        (diagonal_from_top_right == SEARCH_PATTERN_2 or diagonal_from_top_right == SEARCH_PATTERN_2[::-1])

data = read_data(4)

search_occurences = 0
for i in range(len(data)):
    for j in range(len(data[0])):
        if check_for_match(data, i, j):
            search_occurences += 1

print(search_occurences)
