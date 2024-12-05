from functools import cmp_to_key
from utils import read_data


# Shared input processing

data = read_data(5)
separator_index = data.index("")
rules_as_str = [line.split("|") for line in data[ : separator_index]]
rules = [(int(left), int(right)) for (left, right) in rules_as_str]
updates_as_str = [line.split(",") for line in data[separator_index + 1 : ]]
updates = [[int(number) for number in update] for update in updates_as_str]


# Part 1

result = 0
for update in updates:
    rules_are_upheld = True
    for (left, right) in rules:
        if left not in update or right not in update:
            continue
        if update.index(left) > update.index(right):
            rules_are_upheld = False
            break
    if rules_are_upheld:
        result += update[int((len(update) - 1) / 2)]

print(result)


# Part 2

def compare(x, y):
    for rule in rules:
        if x in rule and y in rule:
            return rule.index(x) - rule.index(y)

result = 0
for update in updates:
    sorted_update = sorted(update, key=cmp_to_key(compare))
    if update != sorted_update:
        result += sorted_update[int((len(update) - 1) / 2)]
print(result)
