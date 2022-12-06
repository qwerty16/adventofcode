from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += line.strip()
    return output


def main(input_file_path, length):
    data = read_file(input_file_path)
    for i in range(length, len(data)):
        marker = set(data[i - length : i])
        if len(marker) == length:
            return i


print("### Part 1")
test_output = main(test_input_file_path, 4)
print(f"Test: {test_output}\t\tShould be: 7")
actual_output = main(input_file_path, 4)
print(f"Actual: {actual_output}\t\tShould be: 1625")

print("### Part 2")
test_output = main(test_input_file_path, 14)
print(f"Test: {test_output}\t\tShould be: 19")
actual_output = main(input_file_path, 14)
print(f"Actual: {actual_output}\t\tShould be: 2250")
