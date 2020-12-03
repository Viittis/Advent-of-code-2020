# https://adventofcode.com/2020/day/3
import numpy as np
import pandas as pd


# External data file
#data_in = 'data.txt'
data_in = 'sample.txt'


# Read every line from a txt file into a numpy array
def load_data(file_in):
    df = pd.read_csv(data_in, sep="", header=None)

    return df


# xx
def check_for_trees(row, idx):
    if row[idx] == '#':  # If we encounter a tree
        print(row, idx)
        return 1
    else:
        print(row, idx)
        return 0


# Main
def main():

    arr_data = load_data(data_in)
    print(arr_data)
    exit()

    pos_x = 0
    trees_hit = 0

    for row in row_data:
        last_pos = len(row)-1
        steps_left = last_pos-pos_x
        if steps_left >= 3:
            pos_x += 3
            trees_hit += check_for_trees(row, pos_x)
        else:
            pos_x = 3 + steps_left
            trees_hit += check_for_trees(row, pos_x)

    print(f'Number of trees encountered {trees_hit}')

if __name__ == '__main__':
    main()