from pathlib import Path

input_file_path = Path(__file__).absolute().parent / "test_input.txt"

with open(input_file_path, 'r') as input_file:
    for line in input_file.readlines():
        line = line.strip()