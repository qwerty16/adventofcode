from os import linesep
from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

def file_to_list(input_file_path):
    output = []
    with open(input_file_path, 'r') as input_file:
        for line in input_file.readlines():
            output += [[line.strip(), 0]]
    
    return output

def process_instruction(current_line, instruction):
    next_line = 0
    accumulator_change = 0
    return next_line, accumulator_change

def run_console_code(input_file_path):
    accumulator = 0
    instructions = file_to_list(input_file_path)
    current_line = 0
    current_instruction = instructions[current_line][0]
    while instructions[current_line][1] == 0:
        instructions[current_line][1] += 1
        next_line, accumulator_change = process_instruction(current_line, current_instruction)
        accumulator += accumulator_change
        current_line = next_line
    
    return accumulator


### Part 1
test_output = run_console_code(test_input_file_path)
#actual_output = run_console_code(input_file_path)
print(f"Test: {test_output}\t\tShould be: 5")
#print(f"Actual: {actual_output}")

# >>> e = [['a', 0], ['b', 0], ['c', 0]]
# >>> e[0]
# ['a', 0]
# >>> e[0][0]
# 'a'
# >>> e[0][1] 
# 0
# >>> e[0][1] = 1
# >>> e
# [['a', 1], ['b', 0], ['c', 0]]