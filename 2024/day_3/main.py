from pathlib import Path
import re

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += line.strip()
    return "".join(output)


def main(input_file_path, part):
    data = read_file(input_file_path)

    search_string = "mul\((\d+),(\d+)\)"

    matches = re.findall(search_string, data)

    output = 0
    for match in matches:
        output += int(match[0]) * int(match[1])

    return output


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 161")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}")

print("### Part 2")
# test_output = main(test_input_file_path,2)
# print(f"Test: {test_output}\t\tShould be: XXX")
# actual_output = main(input_file_path,2)
# print(f"Actual: {actual_output}")
