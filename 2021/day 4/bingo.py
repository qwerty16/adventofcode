from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def winning_board(board):
    for line in board:
        if line == [None, None, None, None, None]:
            return True

    rows = range(5)
    columns = range(5)

    for column in columns:
        # print(f"col: {column}")
        count = 0
        for row in rows:
            if board[row][column] is not None:
                break
            else:
                count += 1
            if count == 5:
                return True

    return False


def remove_from_board(number, board):
    return [[value if value != number else None for value in line] for line in board]


def slowest_winner(input_file_path):
    numbers_to_call, bingo_boards = bingo_setup(input_file_path)
    winner = []

    live_boards = list(range(len(bingo_boards)))

    while True:
        called_number = numbers_to_call.pop()
        for board_number in live_boards:
            bingo_boards[board_number] = remove_from_board(called_number, bingo_boards[board_number])
            if winning_board(bingo_boards[board_number]) is True:
                winner = bingo_boards[board_number]
                winning_number = board_number
        if winner != []:
            if len(live_boards) > 0:
                live_boards.remove(winning_number)
            if len(live_boards) == 0:
                return calculate_score(winner, called_number)
            winner = []


def fastest_winner(input_file_path):
    numbers_to_call, bingo_boards = bingo_setup(input_file_path)
    winner, called_number = next_winner(numbers_to_call, bingo_boards)
    return calculate_score(winner, called_number)


def next_winner(numbers_to_call, bingo_boards):
    while True:
        called_number = numbers_to_call.pop()
        for board_number in range(len(bingo_boards)):
            bingo_boards[board_number] = [[number if number != called_number else None for number in line] for line in bingo_boards[board_number]]
            if winning_board(bingo_boards[board_number]) is True:
                winner = bingo_boards[board_number]
                return winner, called_number


def calculate_score(winner, called_number):
    winning_sum = 0
    for line in winner:
        for element in line:
            if element is not None:
                winning_sum += element

    score = called_number * winning_sum
    return score


def bingo_setup(input_file_path):
    with open(input_file_path) as input_file:
        line1 = input_file.readline().strip()
        input_file.readline()
        lines = input_file.readlines()

    numbers_to_call = [int(number) for number in line1.split(",")]
    numbers_to_call.reverse()
    lines = [line.strip().split() for line in lines if line != "\n"]
    n = 5
    bingo_boards = [lines[i:i + n] for i in range(0, len(lines), n)]
    bingo_boards = [[[int(number) for number in line] for line in board] for board in bingo_boards]
    return numbers_to_call, bingo_boards


print("### Part 1")
test_output = fastest_winner(test_input_file_path)
actual_output = fastest_winner(input_file_path)
print(f"Test: {test_output}\t\tShould be: 4512")
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = slowest_winner(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 1924")
actual_output = slowest_winner(input_file_path)
# print(f"Actual: {actual_output}")
