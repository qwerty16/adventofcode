from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


# lengths
# 5: 2,5
# 6: 0,9


def process_input(input_file_path):
    output = []
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            start, end = line.strip().split("|")
            start = [sorted(segments) for segments in start.split()]
            end = [sorted(segments) for segments in end.split()]
            output += [(start, end)]
    return output


def count1478(input_file_path):
    output = 0
    for segments, display in process_input(input_file_path):
        for number in display:
            if len(number) in (2, 3, 4, 7):
                output += 1
    return output


def segments_to_numbers(segments):
    output = {}
    for i in segments:
        if len(i) == 2:
            output["1"] = i
        elif len(i) == 3:
            output["7"] = i
        elif len(i) == 4:
            output["4"] = i
        elif len(i) == 7:
            output["8"] = i

    for i in output.values():
        segments.remove(i)

    for i in segments:
        if len(i) == 5 and output["1"][0] in i and output["1"][1] in i:
            output["3"] = i
        elif len(i) == 6 and not (output["1"][0] in i and output["1"][1] in i):
            output["6"] = i
        elif (
            len(i) == 6
            and output["4"][0] in i
            and output["4"][1] in i
            and output["4"][2] in i
            and output["4"][3] in i
        ):
            output["9"] = i
        elif len(i) == 6:
            output["0"] = i

    segments.remove(output["3"])
    segments.remove(output["6"])
    # segments.remove(output["0"])
    segments.remove(output["9"])

    for segment in output["8"]:
        if segment not in output["9"]:
            bottom_left = segment

    for i in segments:
        if len(i) == 5 and bottom_left in i:
            output["2"] = i
        elif len(i) == 5 and bottom_left not in i:
            output["5"] = i

    return output


def count_output(input_file_path):
    output = 0
    for segment, display in process_input(input_file_path):
        translator = segments_to_numbers(segment)
        i = ""
        for digit in display:
            for key, value in translator.items():
                if value == digit:
                    i += key

        output += int(i)
    return output


print("### Part 1")
test_output = count1478(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 26")
actual_output = count1478(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = count_output(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 61229")
actual_output = count_output(input_file_path)
print(f"Actual: {actual_output}")
