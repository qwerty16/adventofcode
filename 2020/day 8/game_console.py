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

print(file_to_list(test_input_file_path))


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