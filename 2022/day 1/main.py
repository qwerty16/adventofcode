from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def main(input_file_path, max_n=1):
    top = []
    for i in range(0, max_n):
        top += [0]
    current_n = 0
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            line = line.strip()
            if line == "":
                if current_n > top[0]:
                    top[0] = current_n
                    top.sort()
                current_n = 0
            else:
                current_n += int(line)
    return sum(top[:])


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 24000")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}\t\tShould be: 68442")

print("### Part 2")
test_output = main(test_input_file_path, 3)
print(f"Test: {test_output}\t\tShould be: 45000")
actual_output = main(input_file_path, 3)
print(f"Actual: {actual_output}\t\tShould be: 204837")
