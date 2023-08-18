"""
slices.py:
    - make a new name pointing to the same list
    - make a new copy of a list
    - make a new slice of an existing list
"""

if __name__ == '__main__':
    my_list = [float(x) for x in
               input('\nEnter a sequence of numbers: ').split()]

    print(f'\nmy_list: {my_list}\n')

    print('my_list2 = my_list')
    my_list2 = my_list
    print('my_list.sort()\n')
    my_list.sort()

    print(f'my_list: {my_list}')
    print(f'my_list2: {my_list2}')

    print('\nmy_list2 = my_list[:]\n')
    my_list2 = my_list[:]
    my_list.reverse()
    print(f'my_list.reverse(): {my_list}')
    print(f'my_list2: {my_list2}\n')

    print('my_list3 = my_list2[1:3]')
    my_list3 = my_list2[1:3]
    print(f'my_list3: {my_list3}\n')

    print('my_list3 = my_list2[1:-1]')
    my_list3 = my_list2[1:-1]
    print(f'my_list3: {my_list3}\n')

    print('my_list3 = my_list2[-1:1]')
    my_list3 = my_list2[-1:1]
    print(f'my_list3: {my_list3}\n')

    print('my_list3 = my_list2[:3]')
    my_list3 = my_list2[:3]
    print(f'my_list3 = {my_list2[:3]}\n')

    print('my_list3 = my_list2[3:]')
    my_list3 = my_list2[3:]
    print(f'my_list3 = {my_list2[3:]}\n')

    print('my_list3 = my_list2[:]')
    my_list3 = my_list2[:]
    print(f'my_list3 = {my_list3}')
    print('del my_list[1:3]')
    del my_list[1:3]
    print(f'my_list3 = {my_list3}\n')

    print('del my_list[:]', end=' ')
    del my_list[:]
    print(f'my_list: {my_list}')
    print('del my_list2[:]', end=' ')
    del my_list2[:]
    print(f'my_list2: {my_list2}')
    print('del my_list3[:]', end=' ')
    del my_list3[:]
    print(f'my_list3: {my_list3}\n')
