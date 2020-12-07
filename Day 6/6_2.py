# https://adventofcode.com/2020/day/6


# External data file
data_in = 'data.txt'


# Read every line from a txt file
def load_data(file_in):
    data = []

    with open(file_in) as curfile:
        single_item = []
        for line in curfile.readlines():
            answer = line.rstrip()
            if answer != '':
                single_item.append(answer)
            else:
                data.append(single_item)
                single_item = []
        data.append(single_item)

    return data
    

# Count same answers
def count_repeats(list_in):
    answers = len(list_in)
    str_ans = ''.join(list_in)
    ltrs = set(x for x in str_ans)
    
    valid_answers = 0
    
    for ltr in ltrs:
        if ltr in str_ans:
            ltr_count = str_ans.count(ltr)
            if ltr_count == answers:
                valid_answers += 1

    return valid_answers
    
    
# Main
def main():
    raw_data = load_data(data_in)
    
    total = 0
    
    for group in raw_data:
        total += count_repeats(group)

    print(f'Total is {total}')


if __name__ == '__main__':
    main()