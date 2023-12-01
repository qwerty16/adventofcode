from pathlib import Path
from collections import namedtuple

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

str_numbers = "1234567890"

word_to_char_map = {
    "one": "one1one",
    "two": "two2two",
    "three": "three3three",
    "four": "four4four",
    "five": "five5five",
    "six": "six6six",
    "seven": "seven7seven",
    "eight": "eight8eight",
    "nine": "nine9nine",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
}


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [line.strip()]
    return output


def part_one(data):
    output = 0
    for line in data:
        filtered_line = [x for x in line if x in str_numbers]
        first_last = int(filtered_line[0] + filtered_line[-1])
        output += first_last
    return output


def main(input_file_path, part):
    data = read_file(input_file_path)
    if part == 1:
        return part_one(data)

    elif part == 2:
        output = []
        for line in data:
            output_line = line
            for word, char in word_to_char_map.items():
                output_line = output_line.replace(word, char)
            output += [output_line]

        return part_one(output)


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 142")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 281")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
