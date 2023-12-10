from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [line.strip()]
    return output


def end_location_not_found(current_locations, part):
    if part == 1:
        if current_locations == ["ZZZ"]:
            return False
        return True

    if part == 2:
        for location in current_locations:
            if location[-1] != "Z":
                return True
        return False


def main(input_file_path, part):
    data = read_file(input_file_path)
    instructions = data[0]

    data = data[2:]

    documents = {}

    for line in data:
        line = line.replace("(", "").replace(")", "")
        line = line.replace(" ", "")
        start, ends = line.split("=")
        documents[start] = ends.split(",")

    steps = 0

    if part == 1:
        current_locations = ["AAA"]
    if part == 2:
        current_locations = [
            location for location in documents.keys() if location[-1] == "A"
        ]

    while end_location_not_found(current_locations, part):
        direction = instructions[steps % len(instructions)]
        steps += 1

        if direction == "R":
            current_locations = [
                documents[location][1] for location in current_locations
            ]
        elif direction == "L":
            current_locations = [
                documents[location][0] for location in current_locations
            ]
        else:
            raise ValueError(f"Invalid direction {direction}")
        # print(current_locations, steps, direction)

    return steps


# print("### Part 1")
# test_output = main(test_input_file_path, 1)
# print(f"Test: {test_output}\t\tShould be: XXX")
# actual_output = main(input_file_path, 1)
# print(f"Actual: {actual_output}")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 6")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
