from pathlib import Path
from collections import namedtuple
from math import sqrt

Point = namedtuple("Point", ["x", "y", "z"])

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    scanners = []
    beacon = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            line = line.strip()
            if line == "":
                scanners += [beacon]
                beacon = []
            elif line[0] == "-":
                pass
            else:
                x, y, z = line.split(",")
                x = int(x)
                y = int(y)
                z = int(z)
                beacon += [Point(x, y, z)]

    scanners += [beacon]
    beacon = []
    return scanners


def distance_between_points(a: Point, b: Point):
    dx = a.x - b.x
    dy = a.y - b.y
    dz = a.z - b.z
    return sqrt(dx ** 2 + dy ** 2 + dz ** 2)


def main(input_file_path):
    scanners = read_file(input_file_path)
    distances = []
    for scanner in scanners:
        distance = {}
        for a, beacon_a in enumerate(scanner):
            for b, beacon_b in enumerate(scanner):
                if a < b and not (a, b) in distance.keys():
                    print(a, b, beacon_a, beacon_b)
                    distance[(a, b)] = distance_between_points(beacon_a, beacon_b)
        distances += [distance]

    unique_distances = set()
    for index, distance in enumerate(distances):
        for points, value in distance.items():
            unique_distances.add(value)

    return len(unique_distances)


print("### Part 1")
test_output = main(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 79")
# actual_output = main(input_file_path)
# print(f"Actual: {actual_output}")

print("### Part 2")
# test_output = main(test_input_file_path)
# print(f"Test: {test_output}\t\tShould be: XXX")
# actual_output = main(input_file_path)
# print(f"Actual: {actual_output}")
