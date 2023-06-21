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


def literal_to_memory(string):
    string = string[1:-1]
    # string = string.replace(r"\\", "a")
    # string = string.replace(r"\"", "a")
    string = re.sub(r"\\\\", "g", string)
    string = re.sub(r"\\\"", "h", string)
    string = re.sub(r"\\x..", "i", string)
    return len(string)


def literal_to_encoded(string):
    string = re.sub(r"\\", "gg", string)
    string = re.sub(r"\"", "hh", string)
    return len(string) + 2


def main(input_file_path, part=1):
    data = read_file(input_file_path)
    if part == 1:
        literal_characters = 0
        memory_characters = 0

        for line in data:
            literal_characters += len(line)
            memory_characters += literal_to_memory(line)
        return literal_characters - memory_characters
    if part == 2:
        literal_characters = 0
        encoded_characters = 0

        for line in data:
            literal_characters += len(line)
            encoded_characters += literal_to_encoded(line)
        return encoded_characters - literal_characters


print("### Part 1")
test_output = main(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 12")
actual_output = main(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 19")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
