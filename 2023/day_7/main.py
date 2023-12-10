from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

card_map = {
    "A": "C",
    "K": "B",
    "Q": "A",
    "J": "0",
    "T": "9",
    "9": "8",
    "8": "7",
    "7": "6",
    "6": "5",
    "5": "4",
    "4": "3",
    "3": "2",
    "2": "1",
}

translate_map = str.maketrans(card_map)


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [line.strip().split()]
    return output


def main(input_file_path, part):
    data = read_file(input_file_path)

    scored_hands = []

    for hand, bid in data:
        score = "0x" + hand.translate(translate_map)
        scored_hands += [[score, hand, bid]]

    print(scored_hands)
    scored_hands.sort()
    print(scored_hands)

    return scored_hands


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 6440")
# actual_output = main(input_file_path,1)
# print(f"Actual: {actual_output}")

print("### Part 2")
# test_output = main(test_input_file_path,2)
# print(f"Test: {test_output}\t\tShould be: XXX")
# actual_output = main(input_file_path,2)
# print(f"Actual: {actual_output}")
