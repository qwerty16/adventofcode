from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def linear_fuel_cost(lst, position):
    distances = []
    for i in lst:
        distances += [abs(i - position)]
    return sum(distances)


def triangular_fuel_cost(lst, position):
    distances = []
    for i in lst:
        n = abs(i - position)
        distances += [(n ** 2 + n) / 2]
    return sum(distances)


def align_crabs(input_file_path, movement="linear"):
    with open(input_file_path) as input_file:
        inp = input_file.readline().strip().split(",")
    crabs = []
    for i in inp:
        crabs += [int(i)]

    previous_cost = 1000000000
    for position in range(max(crabs)):
        if movement == "linear":
            cost = linear_fuel_cost(crabs, position)
        elif movement == "triangular":
            cost = triangular_fuel_cost(crabs, position)
        if cost < previous_cost:
            previous_cost = cost
        else:
            return position - 1, previous_cost


print("### Part 1")
test_output = align_crabs(test_input_file_path)
actual_output = align_crabs(input_file_path)
print(f"Test: {test_output}\t\tShould be: Position 2 Fuel 37")
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = align_crabs(test_input_file_path, movement="triangular")
print(f"Test: {test_output}\t\tShould be: Position 5 Fuel 168")
actual_output = align_crabs(input_file_path, movement="triangular")
print(f"Actual: {actual_output}")
