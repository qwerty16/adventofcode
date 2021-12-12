from networkx import Graph
from networkx.algorithms.simple_paths import all_simple_paths
from pathlib import Path

from networkx.generators import small

test_input_1_file_path = Path(__file__).absolute().parent / "test_input_1.txt"
test_input_2_file_path = Path(__file__).absolute().parent / "test_input_2.txt"
test_input_3_file_path = Path(__file__).absolute().parent / "test_input_3.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"


def read_file(input_file_path):
    g = Graph()
    with open(input_file_path) as input_file:
        for line in input_file.readlines():
            line = line.strip()
            start, end = line.split("-")
            g.add_edge(start, end)
    return g


def simple_paths_revisiting_large_chambers_small_chambers_once(
    G, source, targets, cutoff=200
):
    visited = [source]
    stack = [iter(G[source])]
    while stack:
        children = stack[-1]
        child = next(children, None)
        if child is None:
            stack.pop()
            visited.pop()
        else:
            can_visit = True
            small_revisited = False
            for area in visited:
                if area.isupper() is False and visited.count(area) == 2:
                    small_revisited = True
                    break

            if not child.isupper():
                visit_count = visited.count(child)
                if visit_count == 1 and child in ("start", "end"):
                    can_visit = False
                elif visit_count == 1 and small_revisited is True:
                    can_visit = False
                elif visit_count == 2:
                    can_visit = False

            if can_visit == False:
                continue
            if child in targets:
                yield 1
            visited += [child]
            if targets - set(visited):
                stack.append(iter(G[child]))
            else:
                visited.pop()


def simple_paths_revisiting_large_chambers(G, source, targets, cutoff=200):
    visited = [source]
    stack = [iter(G[source])]
    while stack:
        children = stack[-1]
        child = next(children, None)
        if child is None:
            stack.pop()
            visited.pop()
        else:
            if child in visited and child.isupper() is False:
                continue
            if child in targets:
                yield visited + [child]
            visited += [child]
            if targets - set(visited):
                stack.append(iter(G[child]))
            else:
                visited.pop()


def part_1(input_file_path):
    graph = read_file(input_file_path)
    paths = simple_paths_revisiting_large_chambers(
        graph, source="start", targets={"end"}
    )
    count = 0
    for path in paths:
        count += 1
    return count


def part_2(input_file_path):
    graph = read_file(input_file_path)
    count = 0
    for path in simple_paths_revisiting_large_chambers_small_chambers_once(
        graph, source="start", targets={"end"}
    ):
        count += 1
    return count


print("### Part 1")
test_output = part_1(test_input_1_file_path)
print(f"Test 1: {test_output}\t\tShould be: 10")
test_output = part_1(test_input_2_file_path)
print(f"Test 2: {test_output}\t\tShould be: 19")
test_output = part_1(test_input_3_file_path)
print(f"Test 3: {test_output}\t\tShould be: 226")
actual_output = part_1(input_file_path)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = part_2(test_input_1_file_path)
print(f"Test 1: {test_output}\t\tShould be: 36")
test_output = part_2(test_input_2_file_path)
print(f"Test 2: {test_output}\t\tShould be: 103")
test_output = part_2(test_input_3_file_path)
print(f"Test 3: {test_output}\t\tShould be: 3509")
actual_output = part_2(input_file_path)
print(f"Actual: {actual_output}")
