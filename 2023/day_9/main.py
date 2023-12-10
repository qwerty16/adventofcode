from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [[int(x) for x in line.strip().split()]]
    return output


def main(input_file_path, part):
    sequences = read_file(input_file_path)

    output = 0

    for sequence in sequences:
        patterns = [sequence]
        while (max(patterns[-1]) != 0) or (min(patterns[-1]) != 0):
            patterns += [
                [
                    patterns[-1][i + 1] - patterns[-1][i]
                    for i in range(len(patterns[-1]) - 1)
                ]
            ]

        if part == 1:
            output += sum([x[-1] for x in patterns])
        elif part == 2:
            output += patterns[0][0]
            add = False
            for i in range(len(patterns[1:])):
                if add:
                    output += patterns[i + 1][0]
                else:
                    output -= patterns[i + 1][0]
                add = not add

    return output


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 114")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 2")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
