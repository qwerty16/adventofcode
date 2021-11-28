from pathlib import Path

test_input_file_path = Path(__file__).absolute().parent / "test_input.txt"
input_file_path = Path(__file__).absolute().parent / "input.txt"

def line_to_baggage_dict(line):
    line = line.strip()
    line = line.replace("bags", "")
    line = line.replace("bag", "")
    line = line.replace(".", "")
    line = line.replace("  ", " ")
    [container, containees] = line.split("contain")
    containees = containees.split(",")    

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

def file_to_baggage_rules(input_file_path):
    baggage_rules = {}
    with open(input_file_path, 'r') as input_file:
        for line in input_file.readlines():
            new_rule = line_to_baggage_dict(line)
            for bag in new_rule.keys():
                if bag in baggage_rules.keys():
                    baggage_rules[bag] += new_rule[bag]
                else:
                    baggage_rules[bag] = new_rule[bag]

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
    baggage_rules = file_to_baggage_rules(input_file_path)
    total = 0
    initial = ['shiny gold']
    bags = bags_that_can_contain(initial, baggage_rules)
    output = len(set(bags))
    return output
    

test_output = bags_that_can_contain_shiny_gold(test_input_file_path)
#actual_output = bags_that_can_contain_shiny_gold(input_file_path)

print(f"Test: {test_output}\tShould be: 126")
#print(f"Actual: {actual_output}")

# initial = 'gold'
# new_bags = bags[gold]
# for bag in new_bags:
# if bag not in containing bags
# containing bags += bag
# repeat