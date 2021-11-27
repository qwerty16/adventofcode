import os

path = os.getcwd()
input_file_path = os.path.join(path, "test_input.txt")

def extract_passports_from_file(input_file_path):
    list_of_passports = []

    with open(input_file_path, 'r') as input_file:
        current_passport = []
        for line in input_file.readlines():
            line = line.strip()
            if line == '':
                current_passport = [" ".join(current_passport)]
                list_of_passports += current_passport
                current_passport = []
            else:
                current_passport += [line]

        # Account for last line
        current_passport = " ".join(current_passport)
        list_of_passports += [current_passport]
        return list_of_passports

def passport_string_to_dict(passport_string):
    passport = {}
    passport_elements = passport_string.split()
    for element in passport_elements:
        [key, value] = element.split(":")
        passport[key] = value
    return passport

def load_passports(input_file_path):
    passports = []

    passport_strings = extract_passports_from_file(input_file_path)
    
    for passport_string in passport_strings:
        passports += [passport_string_to_dict(passport_string)]
    
    return passports

def passport_valid(passport, required, optional):
    for field in required:
        try:
            passport[field]
        except KeyError:
            return False
    
    return True

valid_passports = 0

passports = load_passports(input_file_path)

required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
optional_fields = ("cid")

for passport in passports:
    print(passport)
    if passport_valid(passport, required_fields, optional_fields) == True:
        valid_passports += 1

print(f"Valid passports: {valid_passports}")