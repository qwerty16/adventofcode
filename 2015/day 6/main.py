from pathlib import Path
from collections import namedtuple

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

Point = namedtuple("Point", ["x", "y"])


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [line.strip()]
    return output


def turn_on(lights, light):
    lights[light] = 1
    return lights


def toggle(lights, light):
    if lights[light] == 1:
        lights[light] = 0
    elif lights[light] == 0:
        lights[light] = 1
    else:
        print(f"something strange going on {lights[light]}")
    return lights


def turn_off(lights, light):
    lights[light] = 0
    return lights


def string_to_points(string):
    x, y = string.split(",")
    return Point(int(x), int(y))


def parse_line(line):
    output = []
    if line[0:7] == "turn on":
        output += [turn_on]
        numbers = line[8:]
    elif line[0:6] == "toggle":
        output += [toggle]
        numbers = line[7:]
    elif line[0:8] == "turn off":
        output += [turn_off]
        numbers = line[9:]
    else:
        print(f"line start not recognised: {line}")

    pair_1, pair_2 = numbers.split("through")
    start = string_to_points(pair_1)
    end = string_to_points(pair_2)

    return output + [start, end]


def main(input_file_path):
    data = read_file(input_file_path)
    lights = [0] * 1000000
    for line in data:
        func, start, end = parse_line(line)
        for x in range(start.x, end.x + 1):
            for y in range(start.y, end.y + 1):
                location = (x * 1000) + y
                lights = func(lights, location)
        # print(sum(lights))
    return sum(lights)


print("### Part 1")
test_output = main(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 998996")
actual_output = main(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
# test_output = main(test_input_file_path)
# print(f"Test: {test_output}\t\tShould be: XXX")
# actual_output = main(input_file_path)
# print(f"Actual: {actual_output}")
