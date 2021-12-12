from pathlib import Path

test_input_1_file_path = Path(__file__).absolute().parent / "test_input.txt"
test_input_2_file_path = Path(__file__).absolute().parent / "test_input.txt"
test_input_3_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def main(input_file_path):
    return 0


print("### Part 1")
test_output = main(test_input_1_file_path)
print(f"Test 1: {test_output}\t\tShould be: 10")
test_output = main(test_input_2_file_path)
print(f"Test 2: {test_output}\t\tShould be: 19")
test_output = main(test_input_3_file_path)
print(f"Test 3: {test_output}\t\tShould be: 226")
# actual_output = main(input_file_path)
# print(f"Actual: {actual_output}")

print("### Part 2")
# test_output = main(test_input_1_file_path)
# print(f"Test 1: {test_output}\t\tShould be: XXX")
# test_output = main(test_input_2_file_path)
# print(f"Test 2: {test_output}\t\tShould be: XXX")
# test_output = main(test_input_3_file_path)
# print(f"Test 3: {test_output}\t\tShould be: XXX")
# print(f"Test: {test_output}\t\tShould be: XXX")
# print(f"Actual: {actual_output}")
