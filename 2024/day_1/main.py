from pathlib import Path
from collections import Counter

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = [[], []]
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            numbers = line.strip().split()
            output[0] += [int(numbers[0])]
            output[1] += [int(numbers[1])]
    return output


def main(input_file_path, part):
    data = read_file(input_file_path)
    list_1 = data[0]
    list_2 = data[1]
    list_1.sort()
    list_2.sort()
    output = 0
    if part == 1:
        for n1, n2 in zip(list_1, list_2):
            output += abs(n1 - n2)

    if part == 2:
        list_2_map = Counter(list_2)
        output = sum([n1 * list_2_map[n1] for n1 in list_1])

    return output


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 11")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 31")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
