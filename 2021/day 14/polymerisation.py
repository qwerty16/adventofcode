from pathlib import Path
from collections import Counter

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path: str):
    instructions = {}
    with open(input_file_path) as input_file:
        polymer = [char for char in input_file.readline().strip()]
        input_file.readline()
        for line in input_file.readlines():
            key, value = line.strip().split("->")
            instructions[key.strip()] = value.strip()

    pairs = []
    elements = Counter(polymer)
    for i in range(len(polymer) - 1):
        pairs += [str(polymer[i] + polymer[i + 1])]
    pairs = Counter(pairs)
    return elements, pairs, instructions


def polymerise(elements: Counter, pairs: Counter, instructions: dict):
    # Thanks to https://www.reddit.com/r/adventofcode/comments/rfzq6f/comment/hohimq4/
    for pair, freq in pairs.copy().items():
        pairs[pair] -= freq
        new_element = instructions[pair]
        elements[new_element] += freq
        new_pair_1 = pair[0] + new_element
        new_pair_2 = new_element + pair[1]
        pairs[new_pair_1] += freq
        pairs[new_pair_2] += freq
    return elements, pairs


def main(input_file_path: str, repeats=10):
    elements, pairs, instructions = read_file(input_file_path)
    for i in range(repeats):
        elements, pairs = polymerise(elements, pairs, instructions)

    counter = elements.most_common()
    most = counter[0][1]
    least = counter[-1][1]
    return most - least


print("### Part 1")
test_output = main(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 1588")
actual_output = main(input_file_path)
print(f"Actual: {actual_output}\t\tShould be: 2797")

print("### Part 2")
test_output = main(test_input_file_path, repeats=40)
print(f"Test: {test_output}\t\tShould be: 2188189693529")
actual_output = main(input_file_path, repeats=40)
print(f"Actual: {actual_output}")
