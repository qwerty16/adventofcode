from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [line.strip()]
    return output


def get_priority(character):
    if character == character.lower():
        priority = ord(character) - ord("a") + 1
    else:
        priority = ord(character) - ord("A") + 1 + 26
    return priority


def part_1(data):
    total = 0
    for line in data:
        halfway = int(len(line) / 2)
        c1 = line[:halfway]
        c2 = line[halfway:]
        for character in c1:
            if character in c2:
                total += get_priority(character)
                break
    return total


def part_2(data):
    total = 0
    for i in range(0, len(data), 3):
        elf1, elf2, elf3 = data[i : i + 3]
        for character in elf1:
            if character in elf2 and character in elf3:
                total += get_priority(character)
                break
    return total


def main(input_file_path, part):
    data = read_file(input_file_path)
    if part == 1:
        return part_1(data)
    if part == 2:
        return part_2(data)


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 157")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}\t\tShould be: 7878")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 70")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}\t\tShould be: 2760")
