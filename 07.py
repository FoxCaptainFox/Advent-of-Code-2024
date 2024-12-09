from utils import read_data


# Part 1

def get_possible_values_1(numbers):
    if len(numbers) == 1:
        return numbers
    possible_previous_values= get_possible_values_1(numbers[:-1])
    return [x + numbers[-1] for x in possible_previous_values] + [x * numbers[-1] for x in possible_previous_values]

data = read_data(7)
result = 0
for line in data:
    value = int(line.split(": ")[0])
    numbers = [int(x) for x in line.split(": ")[1].split(" ")]
    if value in get_possible_values_1(numbers):
        result += value
print(result)


# Part 2

def get_possible_values_2(numbers):
    if len(numbers) == 1:
        return numbers
    possible_previous_values= get_possible_values_2(numbers[:-1])
    return [x + numbers[-1] for x in possible_previous_values] + \
        [x * numbers[-1] for x in possible_previous_values] + \
        [int(f"{x}{numbers[-1]}") for x in possible_previous_values]

data = read_data(7)
result = 0
for line in data:
    value = int(line.split(": ")[0])
    numbers = [int(x) for x in line.split(": ")[1].split(" ")]
    if value in get_possible_values_2(numbers):
        result += value
print(result)
