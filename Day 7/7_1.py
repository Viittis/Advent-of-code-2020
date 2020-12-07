# https://adventofcode.com/2020/day/7

# External data file
data_in = 'data.txt'


# Read every line from a txt file into a list
def load_data(file_in):
    data = []
    with open(file_in) as curfile:
        for line in curfile.readlines():
            line = line.rstrip().split('s contain ')
            data.append(line)
    return data


# Parse rules
def parse_rules(list_in):
    dict_out = {}

    for row in list_in:
        key = row[0].rsplit(' ', 1)[0]
        value = [x.rsplit(' ', 1)[0] for x in row[1].split(', ')]
        dict_out[key] = value

    return dict_out


# Loop the rules until no new matches found
def loop_rules(rules, keywords):

    while True:
        for key, value in rules.items():
            # Remove 2 first chars from all strings to make comparing easier
            value = [x[2:] for x in value]

            # If there is a match, save the key and start a new search
            if bool(set(keywords).intersection(value)):
                print(f'kw: {keywords} key:{key} val:{value}')
                keywords.append(key)
                continue

        # No new matches found, break and return results
        break

    return keywords


# Main
def main():
    # Load puzzle data
    raw_data = load_data(data_in)

    # Parse data, return dict
    rules = parse_rules(raw_data)

    # How many bags can contain at least one shiny gold bag?
    keyword = 'shiny gold'
    # How many bags contain shiny golds bags directly
    direct_matches = [key for key, value in rules.items() if keyword in ''.join(value)]

    result = loop_rules(rules, direct_matches)
    print(result)

    print(f'{len(result)} bags can contain at least one {keyword} bag.')


if __name__ == '__main__':
    main()