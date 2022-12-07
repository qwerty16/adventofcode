from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

# Part 1
# max depth of input is 8
#
# Part 2
# total_space used is 40528671
# remaining space = 70000000 - 40528671 = 29471329
# required to delete = 30000000 - 29471329 = 528,671


def main(input_file_path, part):
    target_space = 528671
    if part == 1:
        output = 0
    elif part == 2:
        output = 70000000
    depth = 0
    structure = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            line = line.strip()
            if line == "$ cd ..":
                if part == 1 and structure[depth - 1] != -1:
                    output += structure[depth - 1]
                elif part == 2 and structure[depth - 1] > target_space:
                    output = min(structure[depth - 1], output)
                structure[depth - 1] = 0
                depth -= 1
            elif line[0:4] == "$ cd":
                depth += 1
            else:
                try:
                    size = int(line.split(" ")[0])
                    start = []
                    for level in structure[0:depth]:
                        if part == 1 and level != -1 and level + size <= 100000:
                            start += [level + size]
                            # print(f"adding {size}")
                        elif part == 1:
                            start += [-1]
                        elif part == 2:
                            start += [level + size]

                    structure = start + structure[depth:]

                except ValueError:
                    pass

    return output


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 95437")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}\t\tShould be: 1367870")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 24933642")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}\t\tShould be: 549173")
