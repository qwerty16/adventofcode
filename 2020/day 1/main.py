values = []

with open(r"C:\Users\rarms\Documents\Programming\Python\adventofcode\adventofcode\2020\day 1\input.txt", 'r') as f:
    for line in f.readlines():
        values += [int(line)]

target = 2020

copy1 = values[:]
copy2 = values[:]
copy3 = values[:]

counter = 0

for i in copy1:
    for j in copy2[counter+1:]:
        for k in copy3[counter+2:]:
            result = i + j + k
            if result == target:
                print(f"{i} + {j} + {k} = {result}")
                output = i * j * k
                print(f"{i} * {j} * {k}= {output}")

