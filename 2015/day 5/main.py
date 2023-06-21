from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [line.strip()]
    return output


def contains_three_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    for character in string:
        if character in vowels:
            vowel_count += 1
    if vowel_count >= 3:
        return True

    return False


def contains_double_letter(string):
    for i in range(len(string) - 1):
        character = string[i]
        next_character = string[i + 1]
        if character == next_character:
            return True
    return False


def contains_forbidden_string(string):
    forbidden_strings = ["ab", "cd", "pq", "xy"]
    for i in range(len(string) - 1):
        character = string[i]
        next_character = string[i + 1]
        if character + next_character in forbidden_strings:
            return False
    return True


def repeated_pair(string):
    for i in range(len(string) - 2):
        pair = string[i : i + 2]
        for j in range(i + 2, len(string) - 1):
            next_pair = string[j : j + 2]
            if pair == next_pair:
                return True
    return False


def letter_sandwich(string):
    for i in range(len(string) - 2):
        character = string[i]
        sandwich_character = string[i + 2]
        if character == sandwich_character:
            return True
    return False


def passes_part_1(string):
    if not contains_three_vowels(string):
        return False
    if not contains_double_letter(string):
        return False
    if not contains_forbidden_string(string):
        return False
    return True


def passes_part_2(string):
    if not repeated_pair(string):
        return False
    if not letter_sandwich(string):
        return False
    return True


def main(input_file_path, part=1):
    data = read_file(input_file_path)
    nice_count = 0
    for string in data:
        if part == 1 and passes_part_1(string):
            nice_count += 1
        elif part == 2 and passes_part_2(string):
            nice_count += 1
    return nice_count


print("### Part 1")
test_output = main(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 2")
actual_output = main(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
