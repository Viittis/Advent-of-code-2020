# https://adventofcode.com/2020/day/3
import numpy as np

# External data file
data_in = 'data.txt'


# Read every line from a txt file into a numpy array
def load_data(file_in):
    data = []
    with open(file_in) as curfile:
        for line in curfile.readlines():
            data.append([x for x in line.rstrip()])

    return np.array(data)


# Get char at pos
def get_char_at(arr, row, column):
    column = column % len(arr[0])
    print(f' row={row}, col={column}, char={arr[row][column]}')
    return arr[row][column]


# Main
def main():
    arr = load_data(data_in)

    path = []
    pos_x = 0

    for idx, row in enumerate(arr):
        pos_x += 3
        pos_y = idx+1

        if pos_y < len(arr):
            path.append(get_char_at(arr, pos_y, pos_x))

    trees_hit = len([x for x in path if x == '#'])

    print(f'Number of trees encountered {trees_hit}')


if __name__ == '__main__':
    main()