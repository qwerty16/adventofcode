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
    data = read_file(input_file_path)

    output = 0

    for line in data:
        increasing = "not set"
        safe = True
        one_level_removed = True if part == 1 else False
        last_level_removed = False

        for i in range(len(line) - 1):
            if last_level_removed:
                n1 = line[i - 1]
                last_level_removed = False
            else:
                n1 = line[i]

            n2 = line[i + 1]

            dif = n2 - n1

            current_direction = dif > 0
            step_change = abs(dif)

            if increasing == "not set":
                increasing = current_direction

            if increasing != current_direction:
                safe = False

            if step_change < 1 or step_change > 3:
                safe = False

            if part == 2 and safe is False and one_level_removed is False:
                safe = True
                one_level_removed = True
                last_level_removed = True

        if safe:
            output += 1
        # else:
        #     print(line)

    return output


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 2")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}")


print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 4")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
