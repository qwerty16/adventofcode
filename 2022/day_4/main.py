from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [line.strip()]
    return output


def main(input_file_path, part):
    data = read_file(input_file_path)
    total = 0
    for pair in data:
        [[a_min, a_max], [b_min, b_max]] = [elf.split("-") for elf in pair.split(",")]
        a_min = int(a_min)
        a_max = int(a_max)
        b_min = int(b_min)
        b_max = int(b_max)
        if part == 1:
            if a_min <= b_min and a_max >= b_max or b_min <= a_min and b_max >= a_max:
                total += 1
        if part == 2:
            if (
                a_min >= b_min
                and a_min <= b_max
                or a_max >= b_min
                and a_max <= b_max
                or b_min >= a_min
                and b_min <= a_max
                or b_max >= a_min
                and b_max <= a_max
            ):
                total += 1
    return total


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 2")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}\t\tShould be: 550")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 4")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
