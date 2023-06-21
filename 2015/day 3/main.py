from os import pipe
from pathlib import Path
from collections import namedtuple

input_file_path = Path(__file__).absolute().parent / "input.txt"

Point = namedtuple("Point", ["x", "y"])


def move(location, direction):
    if direction == ">":  # right
        return Point(location.x + 1, location.y)
    elif direction == "<":  # left
        return Point(location.x - 1, location.y)
    elif direction == "^":  # up
        return Point(location.x, location.y + 1)
    elif direction == "v":  # down
        return Point(location.x, location.y - 1)
    else:
        print(f"Error: unable to parse direction {direction}")


def main(input_file_path, part=1):
    visited = set()
    santa_loc = Point(0, 0)
    robo_loc = Point(0, 0)
    santa_moves = False
    with open(input_file_path) as input_file:
        input = input_file.read()

    for direction in input:
        visited.add(santa_loc)
        visited.add(robo_loc)
        santa_moves = not santa_moves
        if santa_moves:
            santa_loc = move(santa_loc, direction)
        else:
            robo_loc = move(robo_loc, direction)
    return len(visited)


actual_output = main(input_file_path)
print(f"Actual: {actual_output}")
