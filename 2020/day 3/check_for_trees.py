import os

path = os.getcwd()
input_file_path = os.path.join(path, "input.txt")

position = 0
total = 0

with open(input_file_path) as input_file:
    for line in input_file.readlines():
        line = line.strip()
        target = line[position]
        print(f"Character: {target}")
        if target == "#":
            total += 1
        position += 3
        position = position % len(line)

print(f"Total number of trees: {total}")