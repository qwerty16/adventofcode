from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            winning_numbers, your_numbers = line.strip().split(":")[1].split("|")
            winning_numbers = set([int(n) for n in winning_numbers.split()])
            your_numbers = set([int(n) for n in your_numbers.split()])
            output += [(winning_numbers, your_numbers)]
    return output


def main(input_file_path, part):
    data = read_file(input_file_path)
    output = 0
    all_matches = []
    for card in data:
        winning_numbers, your_numbers = card
        matches = winning_numbers.intersection(your_numbers)
        n_matches = len(matches)
        if part == 1 and n_matches > 0:
            score = pow(2, n_matches - 1)
            output += score

        all_matches += [n_matches]

    if part == 2:
        cards = [1 for n in all_matches]
        for idx, match in enumerate(all_matches):
            if match == 0:
                continue

            for i in range(1, match + 1):
                card_to_change = idx + i
                cards[card_to_change] += cards[idx]

        output = sum(cards)

    return output


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 13")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 30")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
