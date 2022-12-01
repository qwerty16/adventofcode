from os import pipe
from pathlib import Path
from collections import namedtuple

input_file_path = Path(__file__).absolute().parent / "input.txt"

Point = namedtuple("Point", ["x", "y"])


def main(input_file_path, part=1):
    visited = set()
    santa_loc = Point(0, 0)
    robo_loc = Point(0, 0)
    santa_moves = False
    with open(input_file_path) as input_file:
        while True:
            visited.add(santa_loc)
            visited.add(robo_loc)
            santa_moves = not santa_moves
            c = input_file.read(1)
            if santa_moves:
                if not c:
                    break
                elif c == ">":  # right
                    santa_loc = Point(santa_loc.x + 1, santa_loc.y)
                elif c == "<":  # left
                    santa_loc = Point(santa_loc.x - 1, santa_loc.y)
                elif c == "^":  # up
                    santa_loc = Point(santa_loc.x, santa_loc.y + 1)
                elif c == "v":  # down
                    santa_loc = Point(santa_loc.x, santa_loc.y - 1)
            else:
                if not c:
                    break
                elif c == ">":  # right
                    robo_loc = Point(santa_loc.x + 1, santa_loc.y)
                elif c == "<":  # left
                    robo_loc = Point(santa_loc.x - 1, santa_loc.y)
                elif c == "^":  # up
                    robo_loc = Point(santa_loc.x, santa_loc.y + 1)
                elif c == "v":  # down
                    robo_loc = Point(santa_loc.x, santa_loc.y - 1)
    return len(visited)


print("### Part 1")
actual_output = main(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
# actual_output = main(input_file_path)
# print(f"Actual: {actual_output}")
