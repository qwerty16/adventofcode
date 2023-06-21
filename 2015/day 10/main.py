from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output = line.strip()
    return output


def main(input_file_path):
    string = read_file(input_file_path)
    for i in range(50):
        new_string = ""
        previous_count = 0
        previous_character = ""

        for character in string:
            # print(f"{character=}")
            # print(f"{new_string=}")
            if previous_character == "":
                previous_count = 1
                previous_character = character
            elif character == previous_character:
                previous_count += 1
            else:
                # add to string
                new_string += str(previous_count) + previous_character
                previous_count = 1
                previous_character = character

        new_string += str(previous_count) + previous_character
        string = new_string
    return len(string)


print("### Part 1")
# test_output = main(test_input_file_path)
# print(f"Test: {test_output}\t\tShould be: XXX")
actual_output = main(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
# test_output = main(test_input_file_path)
# print(f"Test: {test_output}\t\tShould be: XXX")
# actual_output = main(input_file_path)
# print(f"Actual: {actual_output}")
