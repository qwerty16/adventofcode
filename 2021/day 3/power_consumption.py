from pathlib import Path
from pandas import DataFrame

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def input_to_pos_and_neg(i):
    i = int(i)
    if i == 0:
        return -1
    elif i == 1:
        return 1
    else:
        raise TypeError


def power_consumption(input_file_path):
    file_list = []
    with open(input_file_path) as f:
        for line in f.readlines():
            file_list += [[char for char in line.strip()]]

    df = DataFrame(file_list)
    gamma = ''
    epsilon = ''
    for i in df.columns:
        j = df[i].mode()[0]
        gamma += j
        if j == '0':
            epsilon += '1'
        elif j == '1':
            epsilon += '0'
    gamma = int(gamma, 2)
    epsilon = int(epsilon, 2)
    power_consumption = gamma * epsilon
    return power_consumption


def life_support(input_file_path):
    file_list = []
    with open(input_file_path) as f:
        for line in f.readlines():
            file_list += [[char for char in line.strip()]]

    ox_gen_df = DataFrame(file_list)
    co2_scrub_df = ox_gen_df.copy()

    for column in ox_gen_df.columns:
        values = ox_gen_df[column].value_counts()
        zeroes = values['0']
        ones = values['1']
        if ones >= zeroes:
            value = '1'
        elif ones < zeroes:
            value = '0'
        ox_gen_df = ox_gen_df[ox_gen_df[column] == value]
        if len(ox_gen_df) == 1:
            break

    for column in co2_scrub_df.columns:
        values = co2_scrub_df[column].value_counts()
        zeroes = values['0']
        ones = values['1']
        if ones < zeroes:
            value = '1'
        elif ones >= zeroes:
            value = '0'
        co2_scrub_df = co2_scrub_df[co2_scrub_df[column] == value]
        if len(co2_scrub_df) == 1:
            break

    ox_gen = ox_gen_df.to_string(header=False,
                                 index=False,
                                 index_names=False)
    co2_scrub = co2_scrub_df.to_string(header=False,
                                       index=False,
                                       index_names=False)

    ox_gen = int(ox_gen.replace(" ", ""), 2)
    co2_scrub = int(co2_scrub.replace(" ", ""), 2)

    l_sup = ox_gen * co2_scrub
    return l_sup


print("### Part 1")
test_output = power_consumption(test_input_file_path)
actual_output = power_consumption(input_file_path)
print(f"Test: {test_output}\t\tShould be: 198")
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = life_support(test_input_file_path)
actual_output = life_support(input_file_path)
print(f"Test: {test_output}\t\tShould be: 230")
print(f"Actual: {actual_output}")
