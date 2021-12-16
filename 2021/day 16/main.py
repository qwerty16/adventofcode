from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
test_input_2_file_path = Path(__file__).absolute().parent / "test_input_2.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

byte_lookup = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}

hex_lookup = {
    "0000": "0",
    "0001": "1",
    "0010": "2",
    "0011": "3",
    "0100": "4",
    "0101": "5",
    "0110": "6",
    "0111": "7",
    "1000": "8",
    "1001": "9",
    "1010": "A",
    "1011": "B",
    "1100": "C",
    "1101": "D",
    "1110": "E",
    "1111": "F",
}


def read_file(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            l = []
            for char in line.strip():
                l += [byte_lookup[char]]
            output += ["".join(l)]
    return output


def read_version(data, position):
    return hex_lookup["0" + data[position : position + 3]], position + 3


def read_type(data, position):
    return hex_lookup["0" + data[position : position + 3]], position + 3


def read_literal(data, position):
    output = ""
    while True:
        chunk = data[position : position + 5]
        output += chunk[1:]
        position += 5
        if chunk[0] == "0":
            break
    return int(output, 2), position


def read_int(data, position, length):
    output = data[position : position + length]
    return int(output, 2), position + length


def packet_version(line, position):
    # print(f"p:{position} ", end="")
    v, position = read_version(line, position)
    total_version = [int(v)]
    # print(f"v:{v} ", end="")
    t, position = read_type(line, position)
    # print(f"t:{t} ", end="")
    if t == "4":
        literal, position = read_literal(line, position)
        # print(f"lit:{literal} ", end="")
    else:
        i = line[position]
        position += 1
        # print(f"i:{i} ", end="")
        if i == "0":
            l, position = read_int(line, position, 15)
            # print(f"len:{l} ", end="")
            final = position + l
            while position < final:
                new_version, sub_position = packet_version(line[position:final], 0)
                total_version += new_version
                position += sub_position
        elif i == "1":
            n, position = read_int(line, position, 11)
            # print(f"n:{n} ", end="")
            for i in range(n):
                new_version, position = packet_version(line, position)
                total_version += new_version

    return total_version, position


def part_1(input_file_path):
    data = read_file(input_file_path)
    for line in data:
        position = 0
        version, position = packet_version(line, position)
    return sum(version)


def packet_output(line, position):
    v, position = read_version(line, position)
    t, position = read_type(line, position)
    if t == "4":
        literal, position = read_literal(line, position)
        return literal, position
    else:
        i = line[position]
        position += 1
        operating_values = []
        if i == "0":
            l, position = read_int(line, position, 15)
            final = position + l
            while position < final:
                new_literal, sub_position = packet_output(line[position:final], 0)
                operating_values += [new_literal]
                position += sub_position
        elif i == "1":
            n, position = read_int(line, position, 11)
            for i in range(n):
                new_literal, position = packet_output(line, position)
                operating_values += [new_literal]

    if t == "0":
        return sum(operating_values), position
    elif t == "1":
        output = 1
        for value in operating_values:
            output = output * value
        return output, position
    elif t == "2":
        return min(operating_values), position
    elif t == "3":
        return max(operating_values), position
    elif t == "5":
        if operating_values[0] > operating_values[1]:
            return 1, position
        else:
            return 0, position
    elif t == "6":
        if operating_values[0] < operating_values[1]:
            return 1, position
        else:
            return 0, position
    elif t == "7":
        if operating_values[0] == operating_values[1]:
            return 1, position
        else:
            return 0, position


def part_2(input_file_path):
    data = read_file(input_file_path)
    outputs = []
    for line in data:
        position = 0
        literal, position = packet_output(line, position)
        outputs += [literal]
    return outputs


print("### Part 1")
test_output = part_1(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 31")
actual_output = part_1(input_file_path)
print(f"Actual: {actual_output}\t\tShould be: 847")

print("### Part 2")
test_output = part_2(test_input_2_file_path)
print(f"Test: {test_output}\t\tShould be: [3,54,7,9,1,0,0,1]")
actual_output = part_2(input_file_path)
print(f"Actual: {actual_output}")
