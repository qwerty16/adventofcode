from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [line.strip().split()]
    return output

ROCK = 1
PAPER = 2
SCISSORS = 3
LOSE = 0
DRAW = 3
WIN = 6 

def part_1(data):
    score = 0
    for game in data:
        match game:
            case ("A", "X"): # Rock Rock
                score += ROCK + DRAW
            case ("A", "Y"): # Rock Paper
                score += PAPER + WIN
            case ("A", "Z"): # Rock Scissors
                score += SCISSORS + LOSE
            case ("B", "X"): # Paper Rock
                score += ROCK + LOSE
            case ("B", "Y"): # Paper Paper
                score += PAPER + DRAW
            case ("B", "Z"): # Paper Scissors
                score += SCISSORS + WIN
            case ("C", "X"): # Scissors Rock
                score += ROCK + WIN
            case ("C", "Y"): # Scissors Paper
                score += PAPER + LOSE
            case ("C", "Z"): # Scissors Scissors
                score += SCISSORS + DRAW
    return score

def part_2(data):
    score = 0
    for game in data:
        match game:
            case ("A", "X"): # Rock Lose
                score += SCISSORS + LOSE
            case ("A", "Y"): # Rock Draw
                score += ROCK + DRAW
            case ("A", "Z"): # Rock Win
                score += PAPER + WIN
            case ("B", "X"): # Paper Lose
                score += ROCK + LOSE
            case ("B", "Y"): # Paper Draw
                score += PAPER + DRAW
            case ("B", "Z"): # Paper Win
                score += SCISSORS + WIN
            case ("C", "X"): # Scissors Lose
                score += PAPER + LOSE
            case ("C", "Y"): # Scissors Draw
                score += SCISSORS + DRAW
            case ("C", "Z"): # Scissors Win
                score += ROCK + WIN
    return score

def main(input_file_path, part):
    data = read_file(input_file_path)
    if part == 1:
        return part_1(data)
    else:
        return part_2(data)
    

print("### Part 1")
test_output = main(test_input_file_path,1)
print(f"Test: {test_output}\t\tShould be: 15")
actual_output = main(input_file_path,1)
print(f"Actual: {actual_output}\t\tShould be: 14375")

print("### Part 2")
test_output = main(test_input_file_path,2)
print(f"Test: {test_output}\t\tShould be: 12")
actual_output = main(input_file_path,2)
print(f"Actual: {actual_output}")
