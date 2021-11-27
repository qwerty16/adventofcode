import os

path = os.getcwd()
input_file_path = os.path.join(path, "input.txt")

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

def byr_valid(value):
    # Birth Year must be 4 digits between 1920 and 2002
    value = int(value)
    if value <= 2002 and value >= 1920:
        return True
    else:
        return False

def iyr_valid(value):
    #(Issue Year) - four digits; at least 2010 and at most 2020.
    value = int(value)
    if value <= 2020 and value >= 2010:
        return True
    else:
        return False

def eyr_valid(value):
    #(Expiration Year) - four digits; at least 2020 and at most 2030
    value = int(value)
    if value <= 2030 and value >= 2020:
        return True
    else:
        return False

def hgt_valid(value):
    return True

def hcl_valid(value):
    return True

def ecl_valid(value):
    #(Eye Color) - exactly one of: amb blu brn gry grn hzl oth
    if value in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
        return True
    else:
        return False

def pid_valid(value):
    #(Passport ID) - a nine-digit number, including leading zeroes
    if len(value) != 9:
        return False

    int(value)
    return True

def passport_valid(passport):
    required_fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    optional_fields = ("cid")

    is_valid = {
        "byr": byr_valid,
        "iyr": iyr_valid,
        "eyr": eyr_valid,
        "hgt": hgt_valid,
        "hcl": hcl_valid,
        "ecl": ecl_valid,
        "pid": pid_valid
    }

    for field in required_fields:
        try:
            value = passport[field]
        except KeyError:
            return False
    
        if is_valid[field](value) == False:
            return False

    return True

valid_passports = 0

passports = load_passports(input_file_path)

for passport in passports:
    if passport_valid(passport) == True:
        valid_passports += 1

print(f"Valid passports: {valid_passports}")