from pathlib import Path
import itertools

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
real_input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            raw_line = line.split(",")
            output += [int(x) for x in raw_line]
    return output


def process(data, instruction_pointer):
    continue_processing = True
    instruction = data[instruction_pointer]

    match instruction:
        case 1:
            n_1 = data[data[instruction_pointer + 1]]
            n_2 = data[data[instruction_pointer + 2]]
            result = n_1 + n_2
            data[data[instruction_pointer + 3]] = result
            new_location = instruction_pointer + 4
            # print(f"{instruction=} {n_1=} + {n_2=} = {result=}")

        case 2:
            n_1 = data[data[instruction_pointer + 1]]
            n_2 = data[data[instruction_pointer + 2]]
            result = n_1 * n_2
            data[data[instruction_pointer + 3]] = result
            new_location = instruction_pointer + 4
            # print(f"{instruction=} {n_1=} * {n_2=} = {result=}")

        case 99:
            continue_processing = False
            new_location = instruction_pointer
            # print(f"{instruction=}")

        case other:
            raise ValueError(f"No instructions found for {instruction=}")

    return data, new_location, continue_processing


def main(input_file_path, part):
    original_data = read_file(input_file_path)

    instruction_pointer = 0
    continue_processing = True

    if part == 1:
        data = original_data.copy()
        if input_file_path == real_input_file_path:
            data[1] = 12
            data[2] = 2

        while continue_processing:
            (data, instruction_pointer, continue_processing) = process(
                data, instruction_pointer
            )
        output = data[0]
        return output

    elif part == 2:
        for input_1, input_2 in itertools.product(range(100), range(100)):
            data = original_data.copy()
            instruction_pointer = 0
            continue_processing = True
            data[1] = input_1
            data[2] = input_2

            while continue_processing:
                (data, instruction_pointer, continue_processing) = process(
                    data, instruction_pointer
                )
            output = data[0]

            if output == 19690720:
                return input_1 * 100 + input_2


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 3500")
actual_output = main(real_input_file_path, 1)
print(f"Actual: {actual_output}")

print("### Part 2")
actual_output = main(real_input_file_path, 2)
print(f"Actual: {actual_output}")
