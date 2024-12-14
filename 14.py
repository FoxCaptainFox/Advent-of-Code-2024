import math
from re import findall
from utils import read_data
from PIL import Image, ImageColor


# Shared logic

MAX_X = 101
MAX_Y = 103

def get_next_robot_positions(positions, velocity):
    new_positions = []
    for robot_index in range(len(positions)):
        position_x, position_y = positions[robot_index]
        velocity_x, velocity_y = velocity[robot_index]
        new_x = (position_x + velocity_x) % MAX_X
        new_y = (position_y + velocity_y) % MAX_Y
        new_positions.append((new_x, new_y))
    return new_positions


# Shared data processing

raw_data= read_data(14)
trimmed_data = [findall("p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", line)[0] for line in raw_data]
initial_robot_positions = [(int(line[0]), int(line[1])) for line in trimmed_data]
robot_velocity = [(int(line[2]), int(line[3])) for line in trimmed_data]


# Part 1

STEP_NUMBER = 100

robot_positions = initial_robot_positions.copy()

for step in range(STEP_NUMBER):
    robot_positions = get_next_robot_positions(robot_positions, robot_velocity)

robot_numbers_per_quarter = [0, 0, 0, 0]
middle_x = (MAX_X - 1) / 2
middle_y = (MAX_Y - 1) / 2

for (position_x, position_y) in robot_positions:
    if position_x < middle_x:
        if position_y < middle_y:
            robot_numbers_per_quarter[0] += 1
        if middle_y < position_y:
            robot_numbers_per_quarter[1] += 1
    if middle_x < position_x:
        if position_y < middle_y:
            robot_numbers_per_quarter[2] += 1
        if middle_y < position_y:
            robot_numbers_per_quarter[3] += 1

result = math.prod(robot_numbers_per_quarter)
print(result)


# Part 2

ARBITRARY_STEP_NUMBER = 10000

def output_step_result(robot_positions, step):
    img = Image.new("RGB", (MAX_X, MAX_Y))
    pixels = img.load()
    for (x, y) in robot_positions:
        pixels[x, y] = ImageColor.getrgb("White")
    img.save(f"14 output/{step + 1}.png")

robot_positions = initial_robot_positions.copy()
for step in range(ARBITRARY_STEP_NUMBER):
    robot_positions = get_next_robot_positions(robot_positions, robot_velocity)
    output_step_result(robot_positions, step)
