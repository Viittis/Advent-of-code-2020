# https://adventofcode.com/2020/day/4


# External data file
data_in = 'data.txt'

# Params
mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
optional_fields = ['cid']


# Read every line from a txt file into a list of strings
def load_data(file_in):
    data = []
    with open(file_in) as curfile:
        single_item = ''
        for line in curfile.readlines():
            if line.rstrip() != '':
                single_item += line.rstrip()
            else:
                data.append(single_item)
                single_item = ''
        data.append(single_item)
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


# Check if all dict keys can be found in mandatory fields
def validate_pp(pp):
    key_list = list(pp.keys())
    validation = all(item in mandatory_fields for item in key_list)

    return validation


# Main
def main():
    raw_data = load_data(data_in)
    pp_list = passports_to_dict(raw_data)

    valid_count = 0

    for pp in pp_list:
        print(pp)
        validated = validate_pp(pp)

        if validated is True:
            valid_count += 1

    print(f'The batch file contained {valid_count} valid passport data.')


if __name__ == '__main__':
    main()