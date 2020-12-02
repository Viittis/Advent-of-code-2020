# https://adventofcode.com/2020/day/1

# External data file
data_in = 'data.txt'

# Find the correct entries
def calc_sums(list_in):
    for value in list_in:
        for multiplier in list_in:
            for multiplier2 in list_in:
                if value+multiplier+multiplier2 == 2020:
                    return value, multiplier, multiplier2

# Read every line from a txt file into an array
def load_data(file_in):
    data = []
    with open(file_in) as curfile:
        for line in curfile.readlines():
            data.append(int(line.rstrip()))
    return data

# Main
def main():

    data = load_data(data_in)

    val1, val2, val3 = calc_sums(data)

    result = val1 * val2 * val3
    print(f'The result is {result}')

if __name__ == '__main__':
    main()