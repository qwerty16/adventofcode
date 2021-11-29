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
    new_bags = []

    for bag in initial:
        print(f"Checking for bags within {bag} bag")
        bag_name = bag[0]

        if bag_name == "empty":
            print("Skipping empty bag")
        elif bag_name in baggage_rules.keys():
            print(bag_name)
            new_bags += baggage_rules[bag_name]
            new_bags = [bag for bag in new_bags if bag != ("empty", 0)]
            print(f"Found: {new_bags}")
            for new_bag in new_bags:
                new_bags += bags_contained([new_bag], baggage_rules)
    return new_bags

def bags_that_shiny_gold_contains(input_file_path):
    baggage_rules = file_to_rules(input_file_path, container_bags)
    print(baggage_rules)
    total = 0
    bags = []
    initial = (('shiny gold',1),)
    bags = bags_contained(initial, baggage_rules)
    print(f"Found bags {bags}")
    
    for bag in bags:
        total += bag[1]
    
    return total


### Part 1
test_output = bags_that_can_contain_shiny_gold(test_input_file_path)
#actual_output = bags_that_can_contain_shiny_gold(input_file_path)
print(f"Test: {test_output}\tShould be: 4")
#print(f"Actual: {actual_output}")

### Part 2
test_output = bags_that_shiny_gold_contains(test_input_file_path)
test_output_2 = bags_that_shiny_gold_contains(test_input_file_path_2)
#actual_output = bags_that_shiny_gold_contains(input_file_path)

print(f"Test: {test_output}\tShould be: 32")
print(f"Test: {test_output_2}\tShould be: 126")
#print(f"Actual: {actual_output}")
