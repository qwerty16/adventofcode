from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [line.strip() + "."]
    return output


VALID_CHARS = "0123456789"
NUMBERS = "0123456789"

GEARS = {}


def symbol_adjacent(x, y, data, middle):
    co_ords = (
        (x + 1, y),
        # (x, y + 1),
        (x - 1, y),
        # (x, y - 1),
        (x + 1, y + 1),
        (x + 1, y - 1),
        (x - 1, y + 1),
        (x - 1, y - 1),
    )

    if not middle:
        # print(f"start of number {x} {y}")
        co_ords += ((x, y - 1),)

    for co_ord in co_ords:
        try:
            if co_ord[0] < 0 or co_ord[1] < 0:
                raise IndexError
            value = data[co_ord[0]][co_ord[1]]
            if value != ".":
                if value == "*":
                    if co_ord in GEARS:
                        GEARS[co_ord] += [value]
                    else:
                        GEARS[co_ord] = [value]

                # print(f"{co_ord} {value}")
                return True
        except IndexError:
            # print(f"Co_ord {co_ord} not in range of grid")
            pass

    # Character after is only engine part if not number or dot
    try:
        if data[x][y + 1] not in VALID_CHARS + ".":
            return True
    except IndexError:
        # print(f"Co_ord {co_ord} not in range of grid")
        pass

    return False


def get_surrounding_characters(word_start, word_end, row, data):
    # left and right of word
    positions = [(row, word_start - 1), (row, word_end + 1)]

    for i in range(word_start - 1, word_end + 2):
        # top row
        positions += [(row + 1, i)]
        # bottom row
        positions += [(row - 1, i)]

    # Exclude invalid positions
    positions = [
        position
        for position in positions
        if position[0] > -1
        and position[0] < len(data)
        and position[1] > -1
        and position[1] < len(data)
    ]

    characters = {}

    for position in positions:
        char = data[position[0]][position[1]]
        # Exclude .
        if char == ".":
            continue
        characters[position] = char

    return characters


def main(input_file_path, part):
    data = read_file(input_file_path)
    output = 0

    gears = {}

    for row, line in enumerate(data):
        word_start = -1
        word_end = -1
        in_word = False
        for column, char in enumerate(line):
            if char in NUMBERS:
                in_word = True
                if word_start == -1:
                    word_start = column

            elif char not in NUMBERS and in_word:
                in_word = False
                word_end = column - 1

                surrounding_characters = get_surrounding_characters(
                    word_start, word_end, row, data
                )

                number = int(data[row][word_start : word_end + 1])

                if part == 1 and surrounding_characters != {}:
                    output += number

                if part == 2:
                    for pos, char in surrounding_characters.items():
                        if char == "*":
                            if pos in gears.keys():
                                gears[pos] += [number]
                            else:
                                gears[pos] = [number]

                word_start = -1
                word_end = -1

    if part == 2:
        for numbers in gears.values():
            if len(numbers) == 2:
                output += numbers[0] * numbers[1]

    return output


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 4361")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 467835")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
