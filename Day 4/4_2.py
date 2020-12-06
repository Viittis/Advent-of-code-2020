# https://adventofcode.com/2020/day/4
import re

# External data file
data_in = 'data.txt'

# Params
mandatory_fields = {'byr': (1920, 2002),
                    'iyr': (2010, 2020),
                    'eyr': (2020, 2030),
                    'hgt':{'cm': (150,193),'in': (59, 76)},
                    'hcl': r'^#[0-9a-f]{6}$',
                    'ecl': ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
                    'pid': r'^[0-9]{9}$'}

optional_fields = ['cid']


# Read every line from a txt file into a list of strings
def load_data(file_in):
    data = []

    with open(file_in) as curfile:
        single_item = ''
        for line in curfile.readlines():
            if line.rstrip() != '':
                single_item += line.rstrip() + ' '
            else:
                data.append(single_item.rstrip())
                single_item = ''
        data.append(single_item.strip())

    return data


# Create a dict per passport
def passports_to_dict(passports_in):
    passports_out = []

    for passport in passports_in:
        passport_data = {}
        fields = passport.split(' ')

        for field in fields:
            key, val = field.split(":", 1)
            passport_data[key] = val

        passports_out.append(passport_data)

    return passports_out


# Validate all fields
def validate_pp(pp):
    key_list = list(pp.keys())
    validation = all(item in key_list for item in mandatory_fields)

    if validation:
        for key, value in pp.items():
            # Get condition for key from dict
            condition = mandatory_fields.get(key)

            # Check values between
            if key in ['byr', 'eyr', 'iyr', 'hgt']:
                if key == 'hgt':
                    if 'cm' in value:
                        rng = condition.get('cm')
                    elif 'in' in value:
                        rng = condition.get('in')
                    else:
                        return False
                    val = int(value[:-2])
                else:
                    val = int(value)
                    rng = condition

                if not rng[0] <= val <= rng[1]:
                    return False

            # Match re
            if key in ['hcl', 'pid']:
                match = re.search(condition, value)
                if not match:
                    return False

            # If not in list
            if key == 'ecl':
                if value not in condition:
                    return False
    else:
        return False

    return True


# Main
def main():
    raw_data = load_data(data_in)
    pp_list = passports_to_dict(raw_data)

    valid_count = 0

    for pp in pp_list:
        validated = validate_pp(pp)

        if validated is True:
            valid_count += 1

    print(f'The batch file contained {valid_count} valid passports.')


if __name__ == '__main__':
    main()