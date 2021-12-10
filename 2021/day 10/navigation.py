from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def import_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [[char for char in line.strip()]]
    return output


def first_unmatched(line):
    return 0


def part1(input_file_path):
    systems = import_file(input_file_path)
    print(systems[0])


print("### Part 1")
test_output = part1(test_input_file_path)
# actual_output = part1(input_file_path)
print(f"Test: {test_output}\t\tShould be: XXX")
# print(f"Actual: {actual_output}")

print("### Part 2")
# test_output = main(test_input_file_path)
# actual_output = main(input_file_path)
# print(f"Test: {test_output}\t\tShould be: XXX")
# print(f"Actual: {actual_output}")
