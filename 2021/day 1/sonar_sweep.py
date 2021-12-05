from os import linesep
from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def count_decreases(input_file_path):
    count = 0
    previous_depth = 100000
    with open(input_file_path, "r") as input_file:
        for line in input_file.readlines():
            current_depth = int(line.strip())
            if current_depth > previous_depth:
                count += 1
            previous_depth = current_depth
    return count


def count_three_scan_moving_average_decreases(input_file_path):
    count = 0
    scan = []
    with open(input_file_path, "r") as input_file:
        for line in input_file.readlines():
            scan += [int(line.strip())]

    scan_len = len(scan)

    for index in range(2, scan_len):
        previous_window = scan[index - 2 : index + 1]
        previous_sum = sum(previous_window)
        current_window = scan[index - 1 : index + 2]
        current_sum = sum(current_window)
        if current_sum > previous_sum:
            count += 1
    return count


def main(input_file_path, function):
    return function(input_file_path)


print("### Part 1")
test_output = main(test_input_file_path, count_decreases)
actual_output = main(input_file_path, count_decreases)
print(f"Test: {test_output}\t\tShould be: 7")
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = main(test_input_file_path, count_three_scan_moving_average_decreases)
actual_output = main(input_file_path, count_three_scan_moving_average_decreases)
print(f"Test: {test_output}\t\tShould be: 5")
print(f"Actual: {actual_output}")
