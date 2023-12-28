from pathlib import Path
import itertools

real_input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            raw_line = line.split(",")
            output += [int(x) for x in raw_line]
    return output


def main(input_file_path):
    original_data = read_file(input_file_path)

    instruction_pointer = 0
    continue_processing = True

    data = original_data.copy()

    while continue_processing:
        (data, instruction_pointer, continue_processing) = process(
            data, instruction_pointer
        )
    output = data[0]
    return output


main(real_input_file_path)
