from pathlib import Path
from collections import namedtuple

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

Draw = namedtuple("Draw", ["red", "green", "blue"])

Game = namedtuple("Game", ["number", "draws"])


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            raw_line = line.strip()
            game_number, draws = raw_line.split(":")
            game_number = int(game_number.replace("Game ", ""))
            output_draws = []
            for draw in draws.strip().split(";"):
                current_draw = Draw(0, 0, 0)
                for cubes in draw.strip().split(","):
                    n_cube, colour = cubes.strip().split(" ")
                    n_cube = int(n_cube)
                    if colour == "red":
                        current_draw = Draw(
                            red=n_cube, green=current_draw.green, blue=current_draw.blue
                        )
                    elif colour == "green":
                        current_draw = Draw(
                            red=current_draw.red, green=n_cube, blue=current_draw.blue
                        )
                    elif colour == "blue":
                        current_draw = Draw(
                            red=current_draw.red, green=current_draw.green, blue=n_cube
                        )
                    else:
                        print(f"strange colour: {colour}")
                output_draws += [current_draw]
            output += [Game(number=game_number, draws=output_draws)]
    return output


def is_valid(game: Game) -> bool:
    max_red = 12
    max_green = 13
    max_blue = 14

    for draw in game.draws:
        if draw.red > max_red or draw.green > max_green or draw.blue > max_blue:
            return False
    return True


def game_power(game: Game) -> Draw:
    max_red = 0
    max_green = 0
    max_blue = 0

    for draw in game.draws:
        if draw.red > max_red:
            max_red = draw.red
        if draw.green > max_green:
            max_green = draw.green
        if draw.blue > max_blue:
            max_blue = draw.blue

    return max_red * max_green * max_blue


def main(input_file_path, part):
    data = read_file(input_file_path)

    output = 0

    if part == 1:
        for game in data:
            if is_valid(game):
                output += game.number

    elif part == 2:
        for game in data:
            output += game_power(game)

    return output


print("### Part 1")
test_output = main(test_input_file_path, 1)
print(f"Test: {test_output}\t\tShould be: 8")
actual_output = main(input_file_path, 1)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 2286")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
