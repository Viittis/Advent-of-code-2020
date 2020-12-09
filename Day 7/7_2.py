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
    # Bag count
    try:
        count = int(bag_in[0])
    except:
        count = 0  # set to 0 if it's not a number

    # Bag name
    bag = bag_in[1]

    bag_out = (count, bag)

    return bag_out


# Loop a single layer
def loop_layer(rules, bag_list):
    found_bags = []

    for bag, children in rules.items():
        # If the current bag is found in the bag_list we need to save necessary details
        if bag in bag_list:
            # Str list of children to list of tuples
            child_bags = [(child[0], child[2:]) for child in children]

            for child in child_bags:
                found_bags.append(parse_bag(child))

    return found_bags


# Loop all the layers until we reach max depth
def loop_rules(rules, keyword):
    keywords = [keyword]
    all_child_bags = []

    while True:
        layer_bags = []
        for keyword in keywords:
            findings = loop_layer(rules, keywords)

            if findings:
                layer_bags.append([keyword, findings])

        # We reached max depth
        if not layer_bags:
            break
        else:
            print(layer_bags)

        keywords = [x[1][1][1] for x in layer_bags]

    return 0


# Main
def main():
    # Load puzzle data
    raw_data = load_data(data_in)

    # Parse data, return dict
    rules = parse_rules(raw_data)

    # How many individual bags does one shiny gold bag contain?
    keyword = 'shiny gold'
    result = loop_rules(rules, keyword)

    print(result)

    #print(f'A {keyword} bag contains {result} individual bags.')


if __name__ == '__main__':
    main()
