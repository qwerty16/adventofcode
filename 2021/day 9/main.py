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


def low_points(input_file_path):
    heat_map = read_file(input_file_path)
    output = 0
    for x, column in enumerate(heat_map):
        for y, value in enumerate(column):
            adj = []
            co_ords = ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1))
            for point in co_ords:
                if point[0] >= 0 and point[1] >= 0:
                    try:
                        adj += [heat_map[point[0]][point[1]]]
                    except IndexError:
                        pass

            if less_than(value, adj):
                output += value + 1

    return output


print("### Part 1")
test_output = low_points(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 15")
actual_output = low_points(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
# test_output = main(test_input_file_path)
# actual_output = main(input_file_path)
# print(f"Test: {test_output}\t\tShould be: XXX")
# print(f"Actual: {actual_output}")
