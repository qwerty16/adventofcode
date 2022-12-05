from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    with open(input_file_path) as input_file:
        blanks = 0
        stacks = [[], [], [], [], [], [], [], [], []]
        instructions = []
        for line in input_file.readlines():
            if line.strip() == "":
                blanks += 1

            elif blanks == 0:
                counter = 0
                for i in range(1, len(line), 4):
                    counter += 1
                    character = line[i]
                    if character.isalpha():
                        stacks[counter - 1] += character

            elif blanks == 1:
                tokens = line.strip().split(" ")
                tokens = [int(tokens[1]), int(tokens[3]), int(tokens[5])]
                instructions += [tokens]
    return stacks, instructions


def part_1(stacks, start, end):
    start -= 1
    end -= 1
    stacks[end].insert(0, stacks[start][0])
    stacks[start].pop(0)
    return stacks


def part_2(stacks, instruction):
    x, start, end = instruction
    start -= 1
    end -= 1
    stacks[end] = stacks[start][0:x] + stacks[end]
    stacks[start] = stacks[start][x:]
    return stacks


def output(stacks):
    response = ""
    for stack in stacks:
        try:
            response += stack[0]
        except IndexError:
            pass
    return response


def main(input_file_path, part):
    stacks, instructions = read_file(input_file_path)
    for instruction in instructions:
        if part == 1:
            for i in range(instruction[0]):
                stacks = part_1(stacks, instruction[1], instruction[2])
        elif part == 2:
            stacks = part_2(stacks, instruction)
    return output(stacks)


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: CMZ")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}\tShould be: TQRFCBSJJ")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: MCD")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}\tShould be: RMHFJNVFP")
