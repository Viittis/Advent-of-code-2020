# https://adventofcode.com/2020/day/2

# External data file
data_in = 'data.txt'


# Read every line from a txt file into a list
def load_data(file_in):
    data = []
    with open(file_in) as curfile:
        for line in curfile.readlines():
            data.append(line.rstrip())
    return data


# Parse source data
def parse_rows(list_in):
    list_out = []
    for row in list_in:
        rw = row.split(' ')  # Yields ['1-3', 'a:', 'abcde']
        rw[1] = rw[1].replace(':', '')
        # Append to new list
        list_out.append(rw)
    return list_out


# Main
def main():

    raw_data = load_data(data_in)
    data = parse_rows(raw_data)

    valid_pws = []

    for row in data:
        pos = row[0].split('-')
        p1 = int(pos[0])-1
        p2 = int(pos[1])-1

        char = row[1]
        pw = row[2]

        if (pw[p1] == char) is not (pw[p2] == char):
            valid_pws.append(pw)

    print(f'Number or valid pws is {len(valid_pws)}')

if __name__ == '__main__':
    main()