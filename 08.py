from itertools import permutations
from utils import read_data


# Shared input processing

data = read_data(8)
frequencies = list(set("".join(data)))
frequencies.remove(".")


# Part 1

antinode_locations_1 = set()

for frequency in frequencies:
    frequency_positions = [(i,j) for i, row in enumerate(data) for j, elem in enumerate(row) if elem == frequency]

    for position_1, position_2 in permutations(frequency_positions, 2):
        antinode_i = position_1[0] + (position_1[0] - position_2[0])
        antinode_j = position_1[1] + (position_1[1] - position_2[1])
        if 0 <= antinode_i < len(data) and 0 <= antinode_j < len(data[0]):
            antinode_locations_1.add((antinode_i, antinode_j))

print(len(antinode_locations_1))


# Part 2

antinode_locations_2 = set()

for frequency in frequencies:
    frequency_positions = [(i,j) for i, row in enumerate(data) for j, elem in enumerate(row) if elem == frequency]
    
    for position_1, position_2 in permutations(frequency_positions, 2):
        step = 0
        while True:
            antinode_i = position_1[0] + step * (position_1[0] - position_2[0])
            antinode_j = position_1[1] + step * (position_1[1] - position_2[1])
            if 0 <= antinode_i < len(data) and 0 <= antinode_j < len(data[0]):
                antinode_locations_2.add((antinode_i, antinode_j))
                step += 1
            else:
                break

print(len(antinode_locations_2))
