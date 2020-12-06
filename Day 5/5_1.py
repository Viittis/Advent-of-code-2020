# https://adventofcode.com/2020/day/5

# External data file
data_in = 'data.txt'


# Read every line from a txt file into a list
def load_data(file_in):
    data = []
    with open(file_in) as curfile:
        for line in curfile.readlines():
            data.append(line.rstrip())
    return data


# Replace B = 1, F = 0 and convert bin_str to int
def get_row(row_in):
    bin_str = row_in.replace('B', '1').replace('F', '0')
    return int(bin_str, 2)


# Replace B = 1, F = 0 and convert bin_str to int
def get_col(col_in):
    bin_str = col_in.replace('R', '1').replace('L', '0')
    return int(bin_str, 2)


# Main
def main():
    boarding_passes = load_data(data_in)

    bp_data = []

    for bp in boarding_passes:
        row = get_row(bp[:7])
        col = get_col(bp[-3:])
        seat_id = row * 8 + col

        bp_data.append([row, col, seat_id])

    seat_ids = [x[2] for x in bp_data]

    print(f'The highest seat ID on a boarding pass is {max(seat_ids)}')


if __name__ == '__main__':
    main()