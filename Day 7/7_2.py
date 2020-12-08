# https://adventofcode.com/2020/day/7

# External data file
data_in = 'sample.txt'


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
def loop_rules(rules, keyword):
    keywords = [keyword]
    total_bags = 0
    while True:
        found_new = False
        for key, value in rules.items():
            # Split value into tuples
            value = [(x[0], x[2:]) for x in value]

            # If there is a match, save the key and start a new search
            if bool(set(keywords).intersection(value)):
                if key not in keywords:
                    keywords.append(key)
                    found_new = True
        # No new matches found, break and return results
        if not found_new:
            keywords.remove(keyword)
            break

    return total_bags


# Main
def main():
    # Load puzzle data
    raw_data = load_data(data_in)

    # Parse data, return dict
    rules = parse_rules(raw_data)

    # How many individual bags does one shiny gold bag contain?
    keyword = 'shiny gold'
    result = loop_rules(rules, keyword)

    print(f'A {keyword} bag contains {result} individual bags.')


if __name__ == '__main__':
    main()
