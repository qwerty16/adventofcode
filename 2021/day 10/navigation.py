from pathlib import Path
from statistics import median

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

OPEN = ("(", "[", "{", "<")
CLOSE = (")", "]", "}", ">")
PAIRS = (("(", ")"), ("[", "]"), ("{", "}"), ("<", ">"))


def import_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [[char for char in line.strip()]]
    return output


def corrupted(line):
    o = []
    for char in line:
        if char in OPEN:
            o.append(char)
        elif char in CLOSE:
            closing = char
            opening = o.pop()
            if (opening, closing) not in PAIRS:
                return closing
        else:
            raise TypeError
    return False


def incomplete(line):
    o = []
    for char in line:
        if char in OPEN:
            o.append(char)
        elif char in CLOSE:
            closing = char
            opening = o.pop()
            if (opening, closing) not in PAIRS:
                return closing
        else:
            raise TypeError
    return o


def part1(input_file_path):
    systems = import_file(input_file_path)
    syntax_error = 0
    for system in systems:
        c1 = corrupted(system)
        if c1 == False:
            continue
        elif c1 == ")":
            syntax_error += 3
        elif c1 == "]":
            syntax_error += 57
        elif c1 == "}":
            syntax_error += 1197
        elif c1 == ">":
            syntax_error += 25137
    return syntax_error


def part2(input_file_path):
    scoring = {"(": 1, "[": 2, "{": 3, "<": 4}
    systems = import_file(input_file_path)
    all_scores = []
    for system in systems:
        if corrupted(system) is False:
            inc = incomplete(system)
            inc.reverse()
            score = 0
            for char in inc:
                score = score * 5
                score += scoring[char]
            all_scores += [score]
    return median(all_scores)


print("### Part 1")
test_output = part1(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 26397")
actual_output = part1(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = part2(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 288957")
actual_output = part2(input_file_path)
print(f"Actual: {actual_output}")
