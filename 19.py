from utils import read_data
from functools import cache


# Shared data processing

raw = read_data(19)
available_patterns = tuple(raw[0].split(", "))
desired_outputs = raw[2:]


# Part 1

@cache
def is_output_possible(available_patterns, desired_output):
    for available_pattern in available_patterns:
        if desired_output.startswith(available_pattern):
            new_desired_output = desired_output[len(available_pattern):]
            if new_desired_output == "":
                return True
            if is_output_possible(available_patterns, new_desired_output):
                return True
    return False

possible_ouputs = [desired_output for desired_output in desired_outputs if is_output_possible(available_patterns, desired_output)]
print(len(possible_ouputs))


# Part 2

@cache
def get_possible_option_number(available_patterns, desired_output):
    result = 0
    for available_pattern in available_patterns:
        if desired_output.startswith(available_pattern):
            new_desired_output = desired_output[len(available_pattern):]
            if new_desired_output == "":
                result += 1
            else:
                result += get_possible_option_number(available_patterns, new_desired_output)
    return result

possible_options_numbers = [get_possible_option_number(available_patterns, desired_output) for desired_output in desired_outputs]
print(sum(possible_options_numbers))
