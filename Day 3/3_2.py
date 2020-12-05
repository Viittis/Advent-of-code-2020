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
    return arr[row][column]


# Main
def main():
    arr = load_data(data_in)

    # Step x, y
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total_trees_hit = []

    # Iterate slopes
    for slope in slopes:
        trees_hit = 0
        pos_x = 0
        pos_y = 0
        # Iterate arr
        for i in range(0, len(arr)-slope[1], slope[1]):
            pos_x += slope[0]
            pos_y += slope[1]

            map_point = get_char_at(arr, pos_y, pos_x)
            if map_point == '#':
                trees_hit += 1

        total_trees_hit.append(trees_hit)
        print(trees_hit)

    print(f'Each slope trees hit multiplied together {np.prod(total_trees_hit, dtype=np.int64)}')


if __name__ == '__main__':
    main()