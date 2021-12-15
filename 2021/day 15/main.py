from os import name
from pathlib import Path
from numpy import inf
from collections import namedtuple
from queue import PriorityQueue

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

Point = namedtuple("Point", ["x", "y"])


def read_file(input_file_path: str):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [[int(char) for char in line.strip()]]
    return output


def adj(x, y, max_x, max_y):
    adj = []
    co_ords = (
        Point(x + 1, y),
        Point(x, y + 1),
        Point(x - 1, y),
        Point(x, y - 1),
    )
    for point in co_ords:
        if max_x > point[0] >= 0 and max_y > point[1] >= 0:
            adj += [point]
    return adj


def lowest_weight_path(data):
    visited = set()
    max_x = len(data[0])
    max_y = len(data)
    source = Point(0, 0)
    target = Point(max_x - 1, max_y - 1)
    tentative_distance = PriorityQueue()
    current = source

    tentative_distance.put((0, source))

    distance, current = tentative_distance.get()

    while current != target:
        print(f"current: {current}\t visited: {len(visited)}")
        for point in adj(current.x, current.y, max_x, max_y):
            if point not in visited:
                tentative_distance.put((distance + data[point.x][point.y], point))

        visited.add(current)
        distance, new = tentative_distance.get()
        while new == current:
            distance, new = tentative_distance.get()

        current = new

    return distance


def main(input_file_path: str):
    data = read_file(input_file_path)
    return lowest_weight_path(data)


print("### Part 1")
test_output = main(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 40")
actual_output = main(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
# test_output = main(test_input_file_path)
# print(f"Test: {test_output}\t\tShould be: XXX")
# actual_output = main(input_file_path)
# print(f"Actual: {actual_output}")
