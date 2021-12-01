from os import linesep
from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

def main(input_file_path):
    return 0

print("### Part 1")
test_output = main(test_input_file_path)
#actual_output = main(input_file_path)
print(f"Test: {test_output}\t\tShould be: 7")
#print(f"Actual: {actual_output}")

print("### Part 2")
test_output = main(test_input_file_path)
#actual_output = main(input_file_path)
print(f"Test: {test_output}\t\tShould be: XXX")
#print(f"Actual: {actual_output}")