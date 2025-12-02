from pathlib import Path
import re

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [line.strip()]
    return output


def main(input_file_path, part):
    data = read_file(input_file_path)

    current_number = 50
    times_reached_0 = 0

    for instruction in data:
        direction = instruction[0]
        amount = int(instruction[1:])
        if direction == "L":
            current_number -= amount
        elif direction == "R":
            current_number += amount
        else:
            raise ValueError(f"Invalid direction: {direction}")

        current_number = current_number % 100

        if current_number == 0:
            times_reached_0 += 1

    return times_reached_0


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 3")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 6")
# actual_output = main(input_file_path,2)
# print(f"Actual: {actual_output}")
