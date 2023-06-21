from pathlib import Path
import hashlib

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        output = input_file.read()
    return output


def main(input_file_path, part=1):
    key = read_file(input_file_path)
    for i in range(0, 104897500):
        md5_input = key + str(i)
        md5 = hashlib.md5(md5_input.encode("utf-8")).hexdigest()
        if md5[0:5] == "00000" and part == 1:
            return i
        elif md5[0:6] == "000000":
            return i
    print("No match found")


print("### Part 1")
test_output = main(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 609043")
actual_output = main(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
