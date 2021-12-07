from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def fuel_cost(lst, position):
    distances = []
    for i in lst:
        distances += [abs(i - position)]
    return sum(distances)


def main(input_file_path):
    with open(input_file_path) as input_file:
        inp = input_file.readline().strip().split(",")
    crabs = []
    for i in inp:
        crabs += [int(i)]

    previous_cost = 1000000000
    for position in range(max(crabs)):
        cost = fuel_cost(crabs, position)
        if cost < previous_cost:
            previous_cost = cost
        else:
            return position - 1, previous_cost


print("### Part 1")
test_output = main(test_input_file_path)
actual_output = main(input_file_path)
print(f"Test: {test_output}\t\tShould be: Position 2 Fuel 37")
print(f"Actual: {actual_output}")

print("### Part 2")
# test_output = main(test_input_file_path)
# actual_output = main(input_file_path)
# print(f"Test: {test_output}\t\tShould be: XXX")
# print(f"Actual: {actual_output}")
