from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            direction, magnitude = line.strip().split(" ")
            magnitude = int(magnitude)
            output += [[direction, magnitude]]
    return output


def adjacent(head, tail):
    if head[0] - tail[0] <= 1 and head[1] - tail[1] <= 1:
        return True
    else:
        return False


def main(input_file_path, part):
    data = read_file(input_file_path)
    positions = [[0, 0] for i in range(part)]
    visited = set()
    for instruction in data:
        for step in range(instruction[1]):
            # Move the head in direction shown
            match instruction[0]:
                case "U":
                    positions[0][0] += 1
                case "D":
                    positions[0][0] -= 1
                case "L":
                    positions[0][1] -= 1
                case "R":
                    positions[0][1] += 1
                case _:
                    print(f"something went wrong instruction: {instruction}")

            for knot in range(part - 1):
                head = positions[knot]
                tail = positions[knot + 1]
                if abs(head[0] - tail[0]) > 1 or abs(head[1] - tail[1]) > 1:
                    if head[0] > tail[0]:
                        positions[knot + 1][0] += 1
                    elif head[0] < tail[0]:
                        positions[knot + 1][0] -= 1

                    if head[1] > tail[1]:
                        positions[knot + 1][1] += 1
                    elif head[1] < tail[1]:
                        positions[knot + 1][1] -= 1

            # Add tail position to visited set
            # print(positions)
            visited.add((positions[-1][0], positions[-1][1]))
    return len(visited)


print("### Part 1")
test_output = main(test_input_file_path, 2)
print(f"Test: {test_output}\t\tShould be: 13")
actual_output = main(input_file_path, 2)
print(f"Actual: {actual_output}\t\tShould be: 5619")

print("### Part 2")
test_output = main(test_input_file_path, 10)
print(f"Test: {test_output}\t\tShould be: 1")
actual_output = main(input_file_path, 10)
print(f"Actual: {actual_output}\t\tShould be: 2376")
