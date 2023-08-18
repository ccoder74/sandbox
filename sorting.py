"""
sorting.py:
    (reverse) sort the list of numbers by using the sort method
    (reverse) sort the list of numbers using the sorted() function
"""

if __name__ == '__main__':
    num_seq = [float(x) for x in
               input('\nEnter a sequence of numbers to be sorted: ').split()]

    print(f'\nUnsorted list: {num_seq}')

    num_seq.sort()
    print(f'num_seq.sort(): {num_seq}')

    num_seq.sort(reverse=True)
    print(f'num_seq.sort(reverse=True): {num_seq}')

    print('\nSorting num_seq again to show the effect of num_seq.reverse()...')
    num_seq.sort()
    print(f'num_seq.sort(): {num_seq}')
    num_seq.reverse()
    print(f'num_seq.reverse(): {num_seq}\n')

    num_seq_sorted = sorted(num_seq)
    print(f'num_seq_sorted = sorted(num_seq): {num_seq_sorted}')

    num_seq_sorted_rev = sorted(num_seq, reverse=True)
    print('num_seq_sorted_rev = sorted(num_seq, reverse = True):')
    print(f'{num_seq_sorted_rev}\n')
