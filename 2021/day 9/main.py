from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for string in input_file.readlines():
            line = []
            for character in string.strip():
                line += [int(character)]
            output += [line]
    return output


def less_than(value, list1):
    for i in list1:
        if value >= i:
            return False
    return True


def adj_points(x, y, heat_map):
    adj = []
    co_ords = ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1))
    for point in co_ords:
        if point[0] >= 0 and point[1] >= 0:
            try:
                adj += [heat_map[point[0]][point[1]]]
            except IndexError:
                pass
    return adj


def low_points(heat_map):
    output = []
    for x, column in enumerate(heat_map):
        for y, value in enumerate(column):
            adj = adj_points(x, y, heat_map)

            if less_than(value, adj):
                output += [value]

    return output


def basin_size(x, y, heat_map):
    pass


def part1(input_file_path):
    heat_map = read_file(input_file_path)
    points = low_points(heat_map)
    risk = 0
    for point in points:
        risk += point + 1
    return risk


def part2(input_file_path):
    heat_map = read_file(input_file_path)
    points = low_points(heat_map)
    basin_sizes = []
    for point in points:
        basin_sizes += [basin_size(point[0], point[1], heat_map)]

    basin_sizes.sort(reverse=True)
    return basin_sizes[0] * basin_sizes[1] * basin_sizes[2]


print("### Part 1")
test_output = part1(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 15")
actual_output = part1(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
# test_output = main(test_input_file_path)
# actual_output = main(input_file_path)
# print(f"Test: {test_output}\t\tShould be: XXX")
# print(f"Actual: {actual_output}")
