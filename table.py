"""
table.py:
    a four-column/four-row table - a two diminesional array (4 x 4)
"""

if __name__ == '__main__':
    table = [['00', '10', '20', '30'],
             ['01', '11', '21', '31'],
             ['02', '12', '22', '32'],
             ['03', '13', '23', '33']]

    print(f'\n{table}')

    for row in range(4):
        print()
        for column in range(4):
            print(table[row][column], end=' ')

    print('\n')
