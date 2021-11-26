import os

path = os.getcwd()
input_file_path = os.path.join(path, "input.txt")

directions = ((1,1), (3,1), (5,1), (7,1), (1,2))
total = []

def trees_in_path(input_path, horizontal_step, vertical_step=1):
    position = 0
    total = 0
    line_number = 0
    with open(input_path) as input_file:
        for line in input_file.readlines():
            if line_number % vertical_step == 0:
                line = line.strip()
                target = line[position]
                if target == "#":
                    total += 1
                position += horizontal_step
                position = position % len(line)
            line_number += 1
    return total

for direction in directions:
    total += [trees_in_path(input_file_path, direction[0], direction[1])]

print(f"Total number of trees: {total}")
answer = total[0] * total[1] * total[2] * total[3] * total[4]
print(f"Answer = {total[0]} * {total[1]} * {total[2]} * {total[3]} * {total[4]} = {answer}")