from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [line.strip().replace("map:", "").split()]
    return [line for line in output if line != []]


def main(input_file_path, part):
    data = read_file(input_file_path)
    seeds = data[0][1:]
    seeds = [int(s) for s in seeds]

    if part == 2:
        part_2_seeds = []

        for i in range(0, len(seeds), 2):
            start_seed = seeds[i]
            len_seeds = seeds[i + 1]
            these_seeds = list(range(start_seed, start_seed + len_seeds))
            part_2_seeds += these_seeds

        seeds = part_2_seeds
        print(len(seeds))
        print(len(list(set(seeds))))
        return seeds

    processes = data[1:]
    maps = []
    latest_process = []
    for process in processes:
        if len(process) == 1 and latest_process != []:
            maps += [latest_process]
            latest_process = []
        elif len(process) != 1:
            latest_process += [process]

    maps += [latest_process]

    current_seed = 0
    lowest_location = 10000000000

    for seed in seeds:
        print(seed)
        current_seed = seed
        for map in maps:
            for map_section in map:
                map_section = [int(m) for m in map_section]
                if current_seed in range(
                    map_section[1], map_section[1] + map_section[2]
                ):
                    offset = map_section[0] - map_section[1]
                    current_seed += offset
                    # print(f"{map_section} match: {offset=} new value {current_seed}")
                    break
                # print(f"{map_section} no match")

        lowest_location = min(current_seed, lowest_location)
    return lowest_location


print("### Part 1")
# test_output = main(test_input_file_path, 1)
# print(f"Test: {test_output}\t\tShould be: 35")
# actual_output = main(input_file_path, 1)
# print(f"Actual: {actual_output}")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 46")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
