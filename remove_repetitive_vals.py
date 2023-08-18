"""
rem_rep_vals.py:
    removes repetitive values from a list
"""

if __name__ == '__main__':
    my_list = [float(x) for x in input('\nEnter seqence of numbers: ').split()]
    my_list.sort()
    temp_list = []

    print('\nSorted sequence of entered numbers:')
    print(my_list)

    for num in my_list:
        if num not in temp_list:
            temp_list.append(num)
        else:
            continue

    my_list = temp_list

    print('\nSorted sequence of entered numbers with unique elements only:')
    print(f'{my_list}\n')
