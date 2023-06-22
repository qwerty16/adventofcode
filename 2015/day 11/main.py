from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output = line.strip()
    return output


def increment(password):
    output = ""
    max_ord = ord("z")
    for i in range(1, len(password) + 1):
        current_character = password[-i]
        current_ord = ord(current_character)
        new_ord = current_ord + 1
        if new_ord > max_ord:
            output = "a" + output
        else:
            return password[:-i] + chr(new_ord) + output


def contains_consecutive_three(password):
    for i in range(len(password) - 2):
        if ord(password[i]) == ord(password[i + 1]) - 1 == ord(password[i + 2]) - 2:
            return True
    return False


def contains_iol(password):
    for character in password:
        if character in ("i", "o", "l"):
            return True
    return False


def contains_two_different_doubles(password):
    first_match = False
    for i in range(len(password) - 3):
        if password[i] == password[i + 1]:
            first_match_character = password[i]
            first_match = True
    if first_match == False:
        return False
    for i in range(2, len(password) - 1):
        if password[i] == password[i + 1] and password[i] != first_match_character:
            return True
    return False


def passes_checks(password):
    if contains_iol(password):
        return False
    if not contains_consecutive_three(password):
        return False
    if not contains_two_different_doubles(password):
        return False
    return True


def main(input_file_path):
    password = read_file(input_file_path)
    password = increment(password)
    while not passes_checks(password):
        password = increment(password)
    return password


actual_output = main(input_file_path)
print(f"Actual: {actual_output}")
