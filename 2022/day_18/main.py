from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [[int(i) for i in line.strip().split(",")] + [6]]
    return output


def adj(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) == 1


def main(input_file_path, part):
    lava = read_file(input_file_path)
    for i in range(len(lava)):
        for j in range(i, len(lava)):
            curr = lava[i]
            comp = lava[j]
            # print(f"curr: {curr} comp: {comp} diff: {diff}")
            if adj(curr, comp):
                lava[i][3] -= 1
                lava[j][3] -= 1
                # print(f"new curr: {curr} comp: {comp}")

    if part == 1:
        return sum([faces for x, y, z, faces in lava])

    lava_cubes = [[x, y, z] for x, y, z, faces in lava]

    max_d = max([x for x, y, z in lava_cubes]) + 1
    min_d = min([x for x, y, z in lava_cubes]) - 1
    # print(f"x min: {min_d} max: {max_d}")

    fog = []
    for x in range(min_d, max_d):
        for y in range(min_d, max_d):
            for z in range(min_d, max_d):
                fog += [[x, y, z]]

    outer_surface = 0

    for cube in fog:
        for lava_cube in lava_cubes:
            if adj(cube, lava_cube):
                outer_surface += 1

    return outer_surface

# print("### Part 1")
# test_output = main(test_input_file_path, 1)
# print(f"Test: {test_output}\t\tShould be: 64")
# actual_output = main(input_file_path, 1)
# print(f"Actual: {actual_output}")


print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 58")
# actual_output = main(input_file_path, 2)
# print(f"Actual: {actual_output}")
