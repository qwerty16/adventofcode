from os import linesep
from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
test_input_file_path_2 = Path(__file__).absolute().parent / "test_input_2.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

def line_to_items(line):
    line = line.strip()
    line = line.replace("bags", "")
    line = line.replace("bag", "")
    line = line.replace(".", "")
    line = line.replace("  ", " ")
    [container, containees] = line.split("contain")
    containees = containees.split(",")   
    return [container, containees]

def container_bags(line):
    container, containees = line_to_items(line)

    output = {}
    bags = []
    for bag in containees:
        bag = bag.strip()
        if bag == "no other":
            bag = ('empty', 0)
        else:
            n_bags = int(bag[:2])
            bag = bag[2:]
            bag = (bag, n_bags)
        bags += [bag]

    container = container.strip()
    if container in output.keys():
        output[container] += bags
    else:
        output[container] = bags
    #print(output)
    return output

def bag_container(line):
    container, containees = line_to_items(line)    

    output = {}
    for bag in containees:
        bag = bag.strip()
        if bag == "no other":
            pass
        else:
            bag = bag[2:]
            container = container.strip()
            if bag in output.keys():
                output[bag] += [container]
            else:
                output[bag] = [container]
    #print(output)
    return output

def file_to_rules(input_file_path, rule):
    baggage_rules = {}
    with open(input_file_path, 'r') as input_file:
        for line in input_file.readlines():
            new_rule = rule(line)
            for key in new_rule.keys():
                if key in baggage_rules.keys():
                    baggage_rules[key] += new_rule[key]
                else:
                    baggage_rules[key] = new_rule[key]

    return baggage_rules    

def bags_that_can_contain(initial_bag, baggage_rules):
    new_bags = []
    #print(initial_bag)
    for bag in initial_bag:
        if bag in baggage_rules.keys():
            new_bags += baggage_rules[bag]
            for new_bag in new_bags:
                new_bags += bags_that_can_contain([new_bag], baggage_rules)
    return new_bags

def bags_that_can_contain_shiny_gold(input_file_path):
    baggage_rules = file_to_rules(input_file_path, bag_container)
    total = 0
    initial = ['shiny gold']
    bags = bags_that_can_contain(initial, baggage_rules)
    output = len(set(bags))
    return output

def bags_contained(initial, baggage_rules):
    # https://www.reddit.com/r/adventofcode/comments/kaf8v6/comment/gfa6yuf/
    if initial not in baggage_rules.keys():
        return 0
    else:
        sum = 0
        for bag_name, bag_count in baggage_rules[initial]:
            sum += bag_count
            sum += bag_count * bags_contained(bag_name, baggage_rules)
    
    return sum 

def bags_that_shiny_gold_contains(input_file_path):
    baggage_rules = file_to_rules(input_file_path, container_bags)
    bags = bags_contained('shiny gold', baggage_rules)
    return bags

### Part 1
test_output = bags_that_can_contain_shiny_gold(test_input_file_path)
#actual_output = bags_that_can_contain_shiny_gold(input_file_path)
print(f"Test: {test_output}\t\tShould be: 4")
#print(f"Actual: {actual_output}")

### Part 2
test_output = bags_that_shiny_gold_contains(test_input_file_path)
test_output_2 = bags_that_shiny_gold_contains(test_input_file_path_2)
actual_output = bags_that_shiny_gold_contains(input_file_path)

print(f"Test: {test_output}\tShould be: 32")
print(f"Test: {test_output_2}\tShould be: 126")
print(f"Actual: {actual_output}")
