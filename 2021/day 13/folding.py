from os import name, read
from pathlib import Path
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Instruction = namedtuple("Instruction", ["direction", "line"])

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path: str):
    points = set()
    instructions = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            if line[0].isnumeric():
                x, y = line.strip().split(",")
                x = int(x)
                y = int(y)
                points.add(Point(x, y))
            elif line[0].isalpha():
                line = line.strip().split(" ")[-1]
                direction, line = line.split("=")
                instructions += [Instruction(direction, int(line))]
            else:
                continue
    return points, instructions


def fold(points: set, instruction: Instruction):
    to_remove = []
    to_add = []

    for point in points:
        if instruction.direction == "x":
            changing = 0
            constant = 1
        elif instruction.direction == "y":
            changing = 1
            constant = 0
        else:
            raise ValueError
        if point[changing] > instruction.line:
            to_remove += [point]
            new_point = [0, 0]
            new_point[constant] = point[constant]
            new_point[changing] = (2 * instruction.line) - point[changing]
            to_add += [Point(new_point[0], new_point[1])]

    # print(f"to_add: {to_add}")
    for point in to_add:
        points.add(point)

    # print(f"to_remove: {to_remove}")
    for point in to_remove:
        points.remove(point)
    return points


def part_1(input_file_path: str):
    points, instructions = read_file(input_file_path)
    points = fold(points, instructions[0])
    return len(points)


def part_2(input_file_path: str):
    points, instructions = read_file(input_file_path)
    for instruction in instructions:
        points = fold(points, instruction)
    matrix = []
    for i in range(6):
        matrix += [40 * ["."]]

    for point in points:
        matrix[point.y][point.x] = "#"

    for line in matrix:
        print("".join(line))
    return 0


print("### Part 1")
test_output = part_1(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 17")
actual_output = part_1(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
print(f"Test should be a square")
part_2(test_input_file_path)
print(f"Actual output should be 8 capital letters")
part_2(input_file_path)
