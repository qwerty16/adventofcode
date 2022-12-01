from pathlib import Path

input_file_path = Path(__file__).absolute().parent / "input.txt"


def main(input_file_path, part=1):
    output = 0
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            a, b, c = line.strip().split("x")
            a = int(a)
            b = int(b)
            c = int(c)
            side_1 = a * b
            side_2 = b * c
            side_3 = c * a
            if part == 1:
                output += (side_1 + side_2 + side_3) * 2  # paper for present
                output += min([side_1, side_2, side_3])  # extra
            elif part == 2:
                sides = sorted([a, b, c])
                output += (sides[0] + sides[1]) * 2  # shortest two sides
                output += a * b * c  # ribbon for bow
    return output


print("### Part 1")
actual_output = main(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
actual_output = main(input_file_path, part=2)
print(f"Actual: {actual_output}")
