from utils import read_data

# Part 1

data_as_str_lines = read_data(1)
data = [[int(n) for n in line.split("   ")] for line in data_as_str_lines]
left_list_sorted = sorted([row[0] for row in data])
right_list_sorted = sorted([row[1] for row in data])

total_distance = 0
for i in range(len(data)):
    total_distance += abs(left_list_sorted[i] - right_list_sorted[i])

print(total_distance)


# Part 2

data_as_str_lines = read_data(1)
data = [[int(n) for n in line.split("   ")] for line in data_as_str_lines]
left_list = [row[0] for row in data]
right_list = [row[1] for row in data]

score = sum([item * right_list.count(item) for item in left_list])
print(score)
