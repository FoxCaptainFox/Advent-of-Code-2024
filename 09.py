from utils import read_file


# Part 1

disc_map = [int(x) for x in read_file(9)]
disc_space = []
last_file_id = 0

for index, value in enumerate(disc_map):
    if index % 2 == 0:
        disc_space += [last_file_id] * value
        last_file_id += 1
    else:
        disc_space += [None] * value

for right_index in reversed(range(len(disc_space))):
    if disc_space[right_index] is None:
        continue
    for left_index in range(right_index):
        if disc_space[left_index] is None:
            disc_space[left_index] = disc_space[right_index]
            disc_space[right_index] = None
            break

result = sum([i * value for i, value in enumerate(disc_space) if value is not None])
print(result)


# Part 2

disc_map = [int(x) for x in read_file(9)]
disc_space = []
last_file_id = 0

for index, value in enumerate(disc_map):
    if index % 2 == 0:
        id = last_file_id
        last_file_id += 1
    else:
        id = None
    disc_space.append({"length": int(value), "id": id, "moved": False})

right_index = len(disc_space)
while right_index > 0:
    right_index -= 1
    if disc_space[right_index]["id"] is None or disc_space[right_index]["moved"]:
        continue
    for left_index in range(right_index):
        if disc_space[left_index]["id"] is not None or \
            disc_space[left_index]["length"] < disc_space[right_index]["length"]:
            continue
        if disc_space[left_index]["length"] == disc_space[right_index]["length"]:
            disc_space[left_index]["id"] = disc_space[right_index]["id"]
            disc_space[left_index]["moved"] = True
            disc_space[right_index]["id"] = None
            break
        right_file = disc_space[right_index].copy()
        disc_space[right_index]["id"] = None
        disc_space[left_index]["length"] -= right_file["length"]
        right_file["moved"] = True
        disc_space.insert(left_index, right_file)
        right_index += 1
        break
    
block_index = 0
result = 0
for file in disc_space:
    for _ in range(file["length"]):
        if file["id"] is not None:
            result += block_index * file["id"]
        block_index += 1
print(result)
