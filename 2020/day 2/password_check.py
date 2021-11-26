import os

path = os.getcwd()
input_file_path = os.path.join(path, "input.txt")

result = 0

correct_passwords = []

def password_meets_rule(rule, password):
    [a, character] = rule.split()
    locations = a.split("-")
    total_found = 0
    for location in locations:
        if password[int(location)] == character:
            total_found += 1
    
    if total_found == 1:
        return True

def password_meets_rule_part_1(rule, password):
    [a, character] = rule.split()
    [min, max] = a.split("-")
    min = int(min)
    max = int(max)
    total = password.count(character)
    if total >= min and total <= max:
        return True
    else:
        return False

with open(input_file_path, 'r') as input_file:
    for line in input_file.readlines():
        line = line.strip()
        [rule, password] = line.split(":")
        if password_meets_rule(rule, password):
            result += 1
            correct_passwords += [line]

print(f"Number of valid passwords: {result}")
print(correct_passwords)