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


# Parse a single bag to tuple (int count, str bag name)
def parse_bag(bag_in):
    try:
        # Bag count
        count = int(bag_in[0])
        # Bag name
        bag = bag_in[1]
    except:
        count = 0  # set to 0 if it's not a number
        bag = ''

    bag_out = (count, bag)

    return bag_out


# Loop a single layer
def loop_layer(rules, bag_list):
    found_bags = {}

    for bag, children in rules.items():
        # If the current bag is found in the bag_list we need to save necessary details
        if bag in bag_list:
            # Str list of children to list of tuples
            child_bags = [(child[0], child[2:]) for child in children]

            cb_list = []
            for child in child_bags:
                cb_list.append(parse_bag(child))

            found_bags[bag] = cb_list

    return found_bags


# Get updated keywords for next loop
def parse_keywords(dict_in):
    keywords = []
    for key, value in dict_in.items():
        for item in value:
            kw = item[1]
            if kw not in keywords:
                keywords.append(kw)

    return keywords


# Loop all the layers until we reach max depth
def loop_rules(rules, keyword):
    keywords = [keyword]
    bags_out = []

    while True:
        findings = loop_layer(rules, keywords)

        if findings:
            # Append findings
            bags_out.append(findings)

            # Set newly found bags as updated keywords for next loop
            keywords = parse_keywords(findings)
        else:
            break

    return bags_out


# Main
def main():
    # Load puzzle data
    raw_data = load_data(data_in)

    # Parse data, return dict
    rules = parse_rules(raw_data)

    # How many individual bags does one shiny gold bag contain?
    keyword = 'shiny gold'
    layers = loop_rules(rules, keyword)

    print(layers)

    # print(f'A {keyword} bag contains {result} individual bags.')


if __name__ == '__main__':
    main()
