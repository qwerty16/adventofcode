from pathlib import Path

input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    level = 0
    step = 0
    with open(input_file_path) as input_file:
        while True:
            step += 1
            c = input_file.read(1)
            if not c:
                break
            elif c == "(":
                level += 1
            elif c == ")":
                level -= 1
                if level == -1:
                    break
    print(step)
    return level


print("### Part 1")
actual_output = read_file(input_file_path)
print(f"Actual: {actual_output}")
