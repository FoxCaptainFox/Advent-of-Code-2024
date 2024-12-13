from re import findall
from utils import read_file
import numpy as np

A_PRESS_PRICE = 3
B_PRESS_PRICE = 1


# Part 1

raw_file = read_file(13)

result = 0
for match in findall("Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", raw_file):
    a_x, a_y, b_x, b_y, prize_x, prize_y = [int(x) for x in match]

    # The task can be written as equation system:
    # a_x * a_presses + b_x * b_presses = prize_x
    # a_y * a_presses + b_y * b_presses = prize_y

    coefficient_matrix = np.array([[a_x, b_x],[a_y, b_y]])
    dependent_variable = np.array([prize_x, prize_y])
    a_presses, b_presses = np.linalg.solve(coefficient_matrix, dependent_variable)

    a_presses, b_presses = round(a_presses, 4), round(b_presses, 4)
    if a_presses.is_integer() and b_presses.is_integer() and \
        0 <= a_presses <= 100 and 0 <= b_presses <= 100:
        result += a_presses * A_PRESS_PRICE + b_presses * B_PRESS_PRICE

print(result)


# Part 2

PRIZE_COORDINATE_SHIFT = 10000000000000

raw_file = read_file(13)

result = 0
for match in findall("Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)", raw_file):
    a_x, a_y, b_x, b_y, prize_x, prize_y = [int(x) for x in match]
    prize_x, prize_y = prize_x + PRIZE_COORDINATE_SHIFT, prize_y + PRIZE_COORDINATE_SHIFT
    
    # The task can be written as equation system:
    # a_x * a_presses + b_x * b_presses = prize_x
    # a_y * a_presses + b_y * b_presses = prize_y

    coefficient_matrix = np.array([[a_x, b_x],[a_y, b_y]])
    dependent_variable = np.array([prize_x, prize_y])
    a_presses, b_presses = np.linalg.solve(coefficient_matrix, dependent_variable)

    a_presses, b_presses = round(a_presses, 4), round(b_presses, 4)
    if a_presses.is_integer() and b_presses.is_integer() and \
        0 <= a_presses and 0 <= b_presses:
        result += a_presses * A_PRESS_PRICE + b_presses * B_PRESS_PRICE

print(result)
