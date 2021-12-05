from pathlib import Path
from collections import namedtuple

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

Point = namedtuple("Point", ['x', 'y'])
Segment = namedtuple("Segment", ['start', 'end'])


def import_lines(path):
    with open(path) as input_file:
        lines = input_file.readlines()
    return lines


def line_segments(lines):
    segments = []
    for line in lines:
        line = line.strip()
        start, end = line.split("->")
        start = start.split(",")
        start = Point(int(start[0]), int(start[1]))
        end = end.split(",")
        end = Point(int(end[0]), int(end[1]))
        segments += [Segment(start, end)]
    return segments


def cardinal_segments(lines):
    segments = line_segments(lines)
    output = []
    for segment in segments:
        if segment.start.x == segment.end.x:
            output += [segment]
        elif segment.start.y == segment.end.y:
            output += [segment]
    return output


def points_in_segment(segment):
    points = []
    if segment.start.x == segment.end.x:
        start = min(segment.start.y, segment.end.y)
        end = max(segment.start.y, segment.end.y) + 1
        for i in range(start, end):
            points += [Point(x=segment.start.x, y=i)]
    elif segment.start.y == segment.end.y:
        start = min(segment.start.x, segment.end.x)
        end = max(segment.start.x, segment.end.x) + 1
        for i in range(start, end):
            points += [Point(x=i, y=segment.start.y)]
    elif segment.start.x < segment.end.x and segment.start.y < segment.end.y:
        points = [segment.start]
        while points[-1] != segment.end:
            points += [Point(points[-1].x + 1, points[-1].y + 1)]
    elif segment.start.x > segment.end.x and segment.start.y > segment.end.y:
        points = [segment.start]
        while points[-1] != segment.end:
            points += [Point(points[-1].x - 1, points[-1].y - 1)]
    elif segment.start.x < segment.end.x and segment.start.y > segment.end.y:
        points = [segment.start]
        while points[-1] != segment.end:
            points += [Point(points[-1].x + 1, points[-1].y - 1)]
    elif segment.start.x > segment.end.x and segment.start.y < segment.end.y:
        points = [segment.start]
        while points[-1] != segment.end:
            points += [Point(points[-1].x - 1, points[-1].y + 1)]
    return points


def get_field():
    field = []
    for x in range(1000):
        new_col = []
        for y in range(1000):
            new_col.append(0)
        field.append(new_col)
    return field


def overlaps(input_file_path, diagonal=False):
    field = get_field()
    lines = import_lines(input_file_path)
    if diagonal is False:
        segments = cardinal_segments(lines)
    else:
        segments = line_segments(lines)

    field = plot_points(field, segments)

    return get_overlaps(field)


def plot_points(field, segments):
    for segment in segments:
        points = points_in_segment(segment)
        for point in points:
            field[point.x][point.y] += 1
    return field


def get_overlaps(field):
    overlaps = 0
    for x in range(len(field)):
        for cell in field[x]:
            if cell > 1:
                overlaps += 1
    return overlaps


print("### Part 1")
test_output = overlaps(test_input_file_path)
print(f"Test: {test_output}\t\tShould be: 5")
actual_output = overlaps(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = overlaps(test_input_file_path, diagonal=True)
print(f"Test: {test_output}\t\tShould be: 12")
actual_output = overlaps(input_file_path, diagonal=True)
print(f"Actual: {actual_output}")
