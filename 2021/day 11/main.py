from os import read
from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_input(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [[int(char) for char in line.strip()]]
    return output


def adj(x, y, octopi):
    adj = []
    co_ords = (
        (x + 1, y),
        (x, y + 1),
        (x - 1, y),
        (x, y - 1),
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x - 1, y - 1),
    )
    for point in co_ords:
        if 10 > point[0] >= 0 and 10 > point[1] >= 0:
            adj += [point]
    return adj


def flash(octopi, flashed):
    for x, row in enumerate(octopi):
        for y, octopus in enumerate(row):
            if flashed[x][y] == 0 and octopus > 9:
                flashed[x][y] = 1
                for point in adj(x, y, octopi):
                    if flashed[point[0]][point[1]] == 0:
                        octopi[point[0]][point[1]] += 1
                        octopi, flashed = flash(octopi, flashed)
                octopi[x][y] = 0

    return octopi, flashed


def step(octopi):
    for x, row in enumerate(octopi):
        for y, octopus in enumerate(row):
            octopi[x][y] = octopus + 1

    flashed = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    octopi, flashed = flash(octopi, flashed)
    flashes = 0
    for row in flashed:
        flashes += sum(row)

    return octopi, flashes


def steps(input_file_path, n=100):
    octopi = read_input(input_file_path)
    flashes = 0
    for i in range(n):
        octopi, new_flashes = step(octopi)
        flashes += new_flashes
    return flashes


def sync_flash(input_file_path):
    octopi = read_input(input_file_path)
    flashes = 0
    steps = 0
    while flashes != 100:
        octopi, flashes = step(octopi)
        steps += 1
    return steps


print("### Part 1")
test_output = steps(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 1656")
actual_output = steps(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = sync_flash(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 195")
actual_output = sync_flash(input_file_path)
print(f"Actual: {actual_output}")
