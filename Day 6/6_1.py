# https://adventofcode.com/2020/day/6


# External data file
data_in = 'data.txt'


# Read every line from a txt file into a list of strings
def load_data(file_in):
    data = []

    with open(file_in) as curfile:
        single_item = ''
        for line in curfile.readlines():
            if line.rstrip() != '':
                single_item += line.rstrip()
            else:
                data.append(single_item.rstrip())
                single_item = ''
        data.append(single_item.strip())

    return data
    

# Count unique answers
def count_uniques(str_in):
    char_list = [x for x in str_in]
    uniques = set(char_list)
    
    return list(uniques)


# Main
def main():
    raw_data = load_data(data_in)
    
    total = 0
    
    for group in raw_data:
        unique_answers = count_uniques(group)
        total += len(unique_answers)

    print(f'Total is {total}')

if __name__ == '__main__':
    main()