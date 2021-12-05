from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def process_line(line):
    line = line.strip()
    direction, magnitude = line.split()
    magnitude = int(magnitude)
    return direction, magnitude


def aim(direction, magnitude, current):
    horizontal, depth, aim = current

    if direction == 'forward':
        horizontal += magnitude
        depth += aim * magnitude
    elif direction == 'down':
        aim += magnitude
    elif direction == 'up':
        aim -= magnitude

    return (horizontal, depth, aim)


def cardinal(direction, magnitude, current):
    horizontal, depth, aim = current

    if direction == 'forward':
        horizontal += magnitude
    elif direction == 'down':
        depth += magnitude
    elif direction == 'up':
        depth -= magnitude

    return (horizontal, depth, aim)


def calculate_distance_traveled(input_file_path, movement):
    horizontal = 0
    depth = 0
    aim = 0

    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            direction, magnitude = process_line(line)
            current = horizontal, depth, aim
            horizontal, depth, aim = movement(direction, magnitude, current)

    return horizontal * depth


print("### Part 1")
test_output = calculate_distance_traveled(test_input_file_path, cardinal)
actual_output = calculate_distance_traveled(input_file_path, cardinal)
print(f"Test: {test_output}\t\tShould be: 150")
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = calculate_distance_traveled(test_input_file_path, aim)
actual_output = calculate_distance_traveled(input_file_path, aim)
print(f"Test: {test_output}\t\tShould be: 900")
print(f"Actual: {actual_output}")
