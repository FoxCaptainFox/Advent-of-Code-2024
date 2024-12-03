from utils import read_file
import re


# Part 1

data = read_file(3)
result = sum([
    int(number_1) * int(number_2) 
    for (number_1, number_2) 
    in re.findall("mul\((\d+),(\d+)\)", data)
])
    
print(result)


# Part 2

data = read_file(3)
result = sum([
    int(number_1) * int(number_2) 
    for (number_1, number_2) 
    in re.findall("mul\((\d+),(\d+)\)", re.sub("don't\(\)[\s\S]*?(do\(\)|$)", "", data))
])

print(result)
