from pathlib import Path
from collections import namedtuple

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

Point = namedtuple("Point", ["row", "column", "value"])
VisitedPoint = namedtuple("Point", ["row", "column", "value", "distance"])


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        row = 0
        for line in input_file.readlines():
            row_values = line.strip()
            output += [row_values]
            column = 0
            for char in row_values:
                if char == "S":
                    start = VisitedPoint(row, column, ord("a"), 0)
                elif char == "E":
                    end = Point(row, column, ord("z"))
                column += 1
            row += 1
    return output, start, end


def neighbours(current, data, visited):
    max_l = len(data)
    neighbours = []
    changes = ((-1, 0), (0, 1), (1, 0), (0, -1))
    for change in changes:
        new_row = change[0] + current.row
        new_col = change[1] + current.column
        new_val = ord(data[new_row][new_col])
        if 0 <= new_row <= max_l and \
           0 <= new_col <= max_l and \
           (new_row, new_col) not in visited and \
           new_val - current.value < 2:
            neighbours += [Point(new_row, new_col, new_val)]
    return neighbours


def main(input_file_path, part):
    data, start, end = read_file(input_file_path)
    visited = set((start.row, start.column))
    current = start
    print(start, end, visited)
    current_neighbours = neighbours(current, data, visited)
    print(current_neighbours)
    return 0


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 31")
# actual_output = main(input_file_path,1)
# print(f"Actual: {actual_output}")

print("### Part 2")
# test_output = main(test_input_file_path,2)
# print(f"Test: {test_output}\t\tShould be: XXX")
# actual_output = main(input_file_path,2)
# print(f"Actual: {actual_output}")
