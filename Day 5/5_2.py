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


# Get differences between two lists, return the missing value
def get_my_seatid(list1, list2):
    diff = list(set(list1) - set(list2))
    return diff[0]


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
    full_range = [item for item in range(min(seat_ids), max(seat_ids)+1)]

    my_seat = get_my_seatid(full_range, seat_ids)

    print(f'The ID of my seat is {my_seat}')


if __name__ == '__main__':
    main()