from typing import Counter
from utils import read_file


# Part 1

stones = [int(x) for x in read_file(11).split(" ")]

for blink in range(10):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
        elif len(str(stone)) % 2 == 0:
            split_index = int(len(str(stone)) / 2)
            new_stones.append(int(str(stone)[ : split_index]))
            new_stones.append(int(str(stone)[split_index : ]))
        else:
            new_stones.append(stone * 2024)
    stones = new_stones
    
print(len(stones))


# Part 2

stones = [int(x) for x in read_file(11).split(" ")]
stone_counts = Counter(stones)

for blink in range(75):
    new_stone_counts = Counter()
    for stone, count in stone_counts.items():
        if stone == 0:
            new_stone_counts[1] += count
        elif len(str(stone)) % 2 == 0:
            split_index = int(len(str(stone)) / 2)
            new_stone_counts[int(str(stone)[ : split_index])] += count
            new_stone_counts[int(str(stone)[split_index : ])] += count
        else:
            new_stone_counts[stone * 2024] += count
    stone_counts = new_stone_counts
    
print(sum(stone_counts.values()))
