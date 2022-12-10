from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [line.strip()]
    return output


def main(input_file_path, part):
    data = read_file(input_file_path)
    output = 0
    X = 1
    instruction = 0
    adding = False
    add_value = 0
    drawing = ''
    for i in range(1, 241):
        # Start of cycle
        # Draw pixel if X within +- 1 of i % 40
        if i % 40 in (X, X+1, X+2):
            drawing += '#'
        else:
            drawing += ' '
        # Read next instruction
        if i in (20, 60, 100, 140, 180, 220):
            output += X * i
        if not adding:
            match data[instruction].split(" "):
                case ("noop",):
                    # print("nothing happening here")
                    instruction += 1
                case ("addx", value):
                    # print(f"preparing to add {value}")
                    adding = True
                    add_value = int(value)
                case _:
                    print(f"Something strange happened")
                    print(f"instruction {instruction}: {data[instruction]}")
        else:
            # print(f"adding {add_value} to X {X}")
            X += add_value
            instruction += 1
            adding = False
    print(drawing[0:40])
    print(drawing[40:80])
    print(drawing[80:120])
    print(drawing[120:160])
    print(drawing[160:200])
    print(drawing[200:240])
    return output


# test_output = main(test_input_file_path, 1)
actual_output = main(input_file_path, 1)
# print(f"Test: {test_output}\t\tShould be: 13140")
print(f"Actual: {actual_output}")
