from pathlib import Path

input_file_path = Path(__file__).absolute().parent / "input.txt"

total = 0

with open(input_file_path, 'r') as input_file:
    group_size = 0
    group_answers = {}
    for line in input_file.readlines():
        line = line.strip()
        if line == '':
            total += len(group_answers)
            group_size = 0
            group_answers = {}           
        else:
            group_size += 1
            answer = line
            for character in answer:
                if character in group_answers.keys():
                    group_answers[character] += 1
                else:
                    group_answers[character] = 1


print(total)