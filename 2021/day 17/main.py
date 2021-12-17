from pathlib import Path

test_target = (range(20, 31), range(-10, -4))
actual_target = (range(169, 207), range(-108, -67))


def step(x, y, v_x, v_y):
    x += v_x
    y += v_y
    v_y -= 1
    if v_x > 0:
        v_x -= 1
    if v_x < 0:
        v_x += 1

    return x, y, v_x, v_y


def fire_probe(v_x, v_y, target):
    hit = False
    max_y = 0
    x = 0
    y = 0
    missed = False
    while missed == False and hit == False:
        x, y, v_x, v_y = step(x, y, v_x, v_y)
        max_y = max(max_y, y)
        if x in target[0] and y in target[1]:
            hit = True
        if x > max(target[0]) or y < min(target[1]):
            missed = True
    return hit, max_y


def max_height(target):
    max_height = 0
    for x in range(max(target[0]) + 1):
        for y in range(min(target[1]), -1 * min(target[1])):
            hit, max_y = fire_probe(x, y, target)
            if hit is True:
                max_height = max(max_height, max_y)
    return max_height


def count_hits(target):
    hits = 0
    for x in range(max(target[0]) + 1):
        for y in range(min(target[1]), -1 * min(target[1])):
            hit, _ = fire_probe(x, y, target)
            if hit is True:
                hits += 1
    return hits


print("### Part 1")
test_output = max_height(test_target)
print(f"Test: {test_output}\t\tShould be: 45")
actual_output = max_height(actual_target)
print(f"Actual: {actual_output}")

print("### Part 2")
test_output = count_hits(test_target)
print(f"Test: {test_output}\t\tShould be: 112")
actual_output = count_hits(actual_target)
print(f"Actual: {actual_output}")
