from os import linesep
from pathlib import Path
from typing import ParamSpecArgs

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

def distance_change(line):
    line = line.strip()
    direction, magnitude = line.split()
    magnitude = int(magnitude)

    horizontal = 0
    depth = 0

    if direction == 'forward':
        horizontal = magnitude
    elif direction == 'down':
        depth = magnitude
    elif direction == 'up':
        depth = -magnitude
    
    return (horizontal, depth)

def calculate_distance_traveled(input_file_path):
    horizontal = 0
    depth = 0

    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            h_change, d_change = distance_change(line)
            horizontal += h_change
            depth += d_change

    return horizontal * depth

print("### Part 1")
test_output = calculate_distance_traveled(test_input_file_path)
actual_output = calculate_distance_traveled(input_file_path)
print(f"Test: {test_output}\t\tShould be: 150")
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = calculate_distance_traveled(test_input_file_path)
#actual_output = calculate_distance_traveled(input_file_path)
print(f"Test: {test_output}\t\tShould be: XXX")
#print(f"Actual: {actual_output}")