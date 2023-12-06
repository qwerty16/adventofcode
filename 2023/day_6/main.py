from pathlib import Path
from math import sqrt, floor

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path, part):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            line_after_colon = line.strip().split(":")[1]
            if part == 1:
                output += [[int(x) for x in line_after_colon.split()]]
            else:
                output += [[int(line_after_colon.replace(" ", ""))]]
    return output


def main(input_file_path, part):
    races = read_file(input_file_path, part)

    output = 1

    for duration, target in zip(races[0], races[1]):
        winning_combos = 0

        start_time = floor(sqrt(target / 10000))

        for time_held in range(start_time, duration):
            time_remaining = duration - time_held
            distance = time_held * time_remaining
            if distance > target:
                winning_combos = duration + 1 - (2 * time_held)
                print(f"min time: {time_held} n_combos: {winning_combos}")
                break

        output = output * winning_combos

    return output


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 288")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 71503")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
