from pathlib import Path
from collections import namedtuple

Logic = namedtuple("Logic", ("divisible_by", "if_true", "if_false"))

monkey_logic_test = (
    Logic(23, 2, 3),
    Logic(19, 2, 0),
    Logic(13, 1, 3),
    Logic(17, 0, 1)
)

monkey_logic = (
    Logic(3, 3, 7),
    Logic(11, 6, 4),
    Logic(7, 0, 7),
    Logic(2, 5, 1),
    Logic(19, 2, 6),
    Logic(5, 1, 4),
    Logic(17, 2, 0),
    Logic(13, 3, 5)
)

lcm = 3 * 11 * 7 * 2 * 19 * 5 * 17 * 13


def boredom(item, rounds):
    if rounds == 20:
        to = int(item / 3)
    else:
        to = item % lcm
    return to


def modify(monkey, item, test):
    if test == True:
        match monkey:
            case 0:
                item = item * 19
            case 1:
                item = item + 6
            case 2:
                item = item * item
            case 3:
                item = item + 3
    elif test == False:
        match monkey:
            case 0:
                item = item * 7
            case 1:
                item = item + 5
            case 2:
                item = item * item
            case 3:
                item = item + 4
            case 4:
                item = item * 17
            case 5:
                item = item + 7
            case 6:
                item = item + 6
            case 7:
                item = item + 3

    return item


def move_to(monkey, item, test):
    if test == True:
        logic = monkey_logic_test
    else:
        logic = monkey_logic

    d = logic[monkey].divisible_by
    if item % d == 0:
        # print(f"Item with worry level {item} is divisible by {d}")
        to = logic[monkey].if_true
    else:
        # print(f"Item with worry level {item} is not divisible by {d}")
        to = logic[monkey].if_false
    # print(f"Monkey throws to monkey {to}")
    return to


def main(rounds, test=False):
    if test == True:
        items = [[79, 98],
                 [54, 65, 75, 74],
                 [79, 60, 97],
                 [74]]
        inspections = [0, 0, 0, 0]
    else:
        items = [[56, 56, 92, 65, 71, 61, 79],
                 [61, 85],
                 [54, 96, 82, 78, 69],
                 [57, 59, 65, 95],
                 [62, 67, 80],
                 [91],
                 [79, 83, 64, 52, 77, 56, 63, 92],
                 [50, 97, 76, 96, 80, 56]]
        inspections = [0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(rounds):
        for monkey in range(len(items)):
            n_items = len(items[monkey])
            inspections[monkey] += n_items
            returned_items = items.copy()
            returned_items[monkey] = []
            for item in items[monkey]:
                item = modify(monkey, item, test)
                item = boredom(item, rounds)
                items[move_to(monkey, item, test)] += [item]
            items = returned_items

    inspections.sort()
    return inspections[-2] * inspections[-1]


print("### Part 1")
test_output = main(20, True)
print(f"Test: {test_output}\t\tShould be: 10605")
actual_output = main(20)
print(f"Actual: {actual_output}")

print("### Part 2")
print(f"LCM: {lcm}")
test_output = main(10000, True)
print(f"Test: {test_output}\t\tShould be: 2713310158")
actual_output = main(10000)
print(f"Actual: {actual_output}")
