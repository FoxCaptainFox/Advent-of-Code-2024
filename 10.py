from utils import read_data


# Part 1

elevation_matrix = read_data(10, as_separate_characters=True, output_type=int)
trailheads = [(i,j) for i, row in enumerate(elevation_matrix) for j, elem in enumerate(row) if elem == 0]

trailhead_scores = []
for trailhead in trailheads:
    current_positions = [trailhead]
    for elevation in range(1, 10):
        next_positions = set()
        for current_i, current_j in current_positions:
            for i_shift, j_shift in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                next_i, next_j = current_i + i_shift, current_j + j_shift
                if 0 <= next_i < len(elevation_matrix) and \
                    0 <= next_j < len(elevation_matrix[0]) and \
                    elevation_matrix[next_i][next_j] == elevation:
                    next_positions.add((next_i, next_j))
        current_positions = list(next_positions)
    trailhead_scores.append(len(current_positions))
print(sum(trailhead_scores))


# Part 2

def get_paths_forward(elevation_matrix, path_to_this_point, current_elevation):
    next_elevation = current_elevation + 1
    if next_elevation > 9:
        return [path_to_this_point]
    
    result = []
    current_i, current_j = path_to_this_point[-1]
    for i_shift, j_shift in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        next_i, next_j = current_i + i_shift, current_j + j_shift
        if 0 <= next_i < len(elevation_matrix) and \
            0 <= next_j < len(elevation_matrix[0]) and \
            elevation_matrix[next_i][next_j] == next_elevation:
            result += get_paths_forward(elevation_matrix, path_to_this_point + [(next_i, next_j)], next_elevation)
    return result

elevation_matrix = read_data(10, as_separate_characters=True, output_type=int)
trailheads = [(i,j) for i, row in enumerate(elevation_matrix) for j, elem in enumerate(row) if elem == 0]

trailhead_ratings = [len(get_paths_forward(elevation_matrix, [trailhead], 0)) for trailhead in trailheads]
print(sum(trailhead_ratings))
