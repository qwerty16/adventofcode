from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += line.strip()
    return output


def main(input_file_path):
    data = read_file(input_file_path)
    return data


print("### Part 1")
test_output = main(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: XXX")
# actual_output = main(input_file_path)
# print(f"Actual: {actual_output}")

print("### Part 2")
# test_output = main(test_input_file_path)
# print(f"Test: {test_output}\t\tShould be: XXX")
# actual_output = main(input_file_path)
# print(f"Actual: {actual_output}")
