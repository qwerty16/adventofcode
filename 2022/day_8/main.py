from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            output += [line.strip()]
    return output


def visible_from_edge(data):
    max_height = len(data)
    visible = [[0 for x in range(max_height)] for x in range(max_height)]
    for i in range(max_height):
        for j in range(max_height):
            target = int(data[i][j])
            # Outer edges
            if i in (0, max_height - 1) or j in (0, max_height - 1):
                visible[i][j] = 1
            else:
                left = [1 for tree in data[i][:j] if int(tree) >= target]
                right = [1 for tree in data[i][j + 1 :] if int(tree) >= target]
                up = [1 for tree in [row[j] for row in data[:i]] if int(tree) >= target]
                down = [
                    1
                    for tree in [row[j] for row in data[i + 1 :]]
                    if int(tree) >= target
                ]
                if sum(left) == 0 or sum(right) == 0 or sum(up) == 0 or sum(down) == 0:
                    visible[i][j] = 1
    return sum(map(sum, visible))


def directional_score(target, trees):
    score = 0
    for tree in trees:
        if int(tree) < target:
            score += 1
        elif int(tree) >= target:
            score += 1
            break
    return score


def max_scenic_score(data):
    max_score = 0
    max_height = len(data)
    for i in range(max_height):
        for j in range(max_height):
            target = int(data[i][j])
            if i == 0:
                up = []
            else:
                up = [row[j] for row in data[i - 1 :: -1]]
            if j == 0:
                left = []
            else:
                left = list(data[i][:j])[::-1]
            left_score = directional_score(target, left)
            right_score = directional_score(target, data[i][j + 1 :])
            up_score = directional_score(target, up)
            down_score = directional_score(target, [row[j] for row in data[i + 1 :]])
            # print(i, j, target, left_score, right_score, up_score, down_score)
            max_score = max(max_score, left_score * right_score * up_score * down_score)
    return max_score


def main(input_file_path, part):
    data = read_file(input_file_path)
    if part == 1:
        return visible_from_edge(data)
    else:
        return max_scenic_score(data)


# print("### Part 1")
# test_output = main(test_input_file_path, 1)
# print(f"Test: {test_output}\t\tShould be: 21")
# actual_output = main(input_file_path, 1)
# print(f"Actual: {actual_output}\t\tShould be: 1669")

print("### Part 2")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 8")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}")
