import os

path = os.getcwd()
input_file_path = os.path.join(path, "input.txt")

def get_first_half(x):
    length = len(x)
    length = int(length / 2)
    return x[:length]

def get_second_half(x):
    length = len(x)
    length = int(length / 2)
    return x[length:]

def get_column(value):
    columns = list(range(8))
    for side in value:
        if side == "L":
            columns = get_first_half(columns)
        elif side == "R":
            columns = get_second_half(columns)
    return columns[0]

def get_row(value):
    rows = list(range(128))
    for side in value:
        if side == "F":
            rows = get_first_half(rows)
        elif side == "B":
            rows = get_second_half(rows)
    return rows[0]

def get_seat_location(boarding_pass):
    row = get_row(boarding_pass[:-3])
    column = get_column(boarding_pass[-3:])
    return (row, column)

def get_seat_id(row, column):
    return (row * 8) + column

# max_seat_id = 0
# min_seat_id = 900

# with open(input_file_path, 'r') as input_file:
#     for line in input_file.readlines():
#         line = line.strip()
#         (row, column) = get_seat_location(line)
#         seat_id = get_seat_id(row, column)
#         if seat_id > max_seat_id:
#             max_seat_id = seat_id
#         if seat_id < min_seat_id:
#             min_seat_id = seat_id

# print(max_seat_id)
# print(min_seat_id)

min_seat_id = 53
max_seat_id = 896

possible_seats = list(range(min_seat_id, max_seat_id + 1))

filled_seats = []

with open(input_file_path, 'r') as input_file:
    for line in input_file.readlines():
        line = line.strip()
        (row, column) = get_seat_location(line)
        seat_id = get_seat_id(row, column)
        filled_seats += [seat_id]

for seat in possible_seats:
    if seat not in filled_seats:
        print(seat)