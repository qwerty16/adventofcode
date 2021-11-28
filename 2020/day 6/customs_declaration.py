from pathlib import Path

input_file_path = Path(__file__).absolute().parent / "input.txt"

total = 0

with open(input_file_path, 'r') as input_file:
    group_size = 0
    group_answers = {}
    for line in input_file.readlines():
        line = line.strip()

        if line == '':
            for answer in group_answers.keys():
                if group_answers[answer] == group_size:
                    total += 1
            #total += len(group_answers)
            print(f"Line: {line}\tSize: {group_size}\tAnswers: {group_answers}\tTotal: {total}")
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
            print(f"Line: {line}\tSize: {group_size}\tAnswers: {group_answers}\tTotal: {total}")



print(total)