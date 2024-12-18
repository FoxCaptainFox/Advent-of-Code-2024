from math import floor
import re
from utils import read_file


# Part 1

def get_combo_value(combo_operand):
    if 0 <= combo_operand <= 3:
        return combo_operand
    elif combo_operand == 4:
        return a
    elif combo_operand == 5:
        return b
    elif combo_operand == 6:
        return c
    else:
        raise Exception("Combo operand 7 is reserved and should not appear in valid programs")

file_as_str = read_file(17)
match = re.findall("\d+", file_as_str)
a, b, c = [int(x) for x in match[:3]]
programs = [int(x) for x in match[3:]]

instruction_pointer = 0
program = []

while True:
    if len(programs) - 1 < instruction_pointer:
        break

    literal_value = combo_operand= programs[instruction_pointer + 1]

    match programs[instruction_pointer]:
        case 0:
            a = floor(a / (2 ** get_combo_value(combo_operand)))
        case 1:
            b = b ^ literal_value
        case 2:
            b = get_combo_value(combo_operand) % 8
        case 3:
            if a != 0:
                instruction_pointer = literal_value
                continue
        case 4:
            b = b ^ c
        case 5:
            program.append(get_combo_value(combo_operand) % 8)
        case 6:
            b = floor(a / (2 ** get_combo_value(combo_operand)))
        case 7:
            c = floor(a / (2 ** get_combo_value(combo_operand)))
    instruction_pointer += 2

print(",".join(str(x) for x in program))


# Part 2

file_as_str = read_file(17)
match = re.findall("\d+", file_as_str)
programs = [int(x) for x in match[3:]]

'''
This is not a general solution.

It is applicable only to my specific case.
For my input the program above can be written as:

for three_bits in A, starting from the right:
    index = three_bits ^ 7
    C = start the same, as original three_bits, go left by index, take three bits
    out three_bits ^ C

Therefore the code below goes from left to right,
checking all possible values for three bits and
saving combinations that are valid so far
'''

possible_results = ["0000000"]
for program in reversed(programs):
    new_possible_results = []
    for possible_result in possible_results:
        for three_bits_value in range(8):
            new_possible_result = possible_result + bin(three_bits_value)[2:].zfill(3)
            c_index = three_bits_value ^ 7
            c = int(new_possible_result[-c_index - 3 : -c_index if c_index != 0 else None], 2)
            if three_bits_value ^ c == program:
                new_possible_results.append(new_possible_result)
    possible_results = new_possible_results

print(min([int(x, 2) for x in possible_results]))
