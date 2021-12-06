from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def count_of_lantern_fish(input_file_path, days=80):
    with open(input_file_path) as input_file:
        inp = input_file.readline().strip().split(",")
    fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for i in inp:
        i = int(i)
        fish[i] += 1
    days = range(days)
    for day in days:
        fish = {
            0: fish[1],
            1: fish[2],
            2: fish[3],
            3: fish[4],
            4: fish[5],
            5: fish[6],
            6: fish[7] + fish[0],
            7: fish[8],
            8: fish[0],
        }
    return sum(fish.values())


print("### Part 1")
test_output = count_of_lantern_fish(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 5934")
actual_output = count_of_lantern_fish(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = count_of_lantern_fish(test_input_file_path, 256)
print(f"Test: {test_output}\t\tShould be: 26984457539")
actual_output = count_of_lantern_fish(input_file_path, 256)
print(f"Actual: {actual_output}")
