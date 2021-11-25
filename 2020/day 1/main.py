values = []

with open("input.txt", 'r') as f:
    for line in f.readlines():
        values += [int(line)]

target = 2020

copy1 = values[:]
copy2 = values[:]

for i in copy1:
    for j in copy2:
        result = i + j
        if result == target:
            print(f"{i} + {j} = {result}")
            output = i * j
            print(f"{i} * {j} = {output}")
    copy2 = copy2[1:]
