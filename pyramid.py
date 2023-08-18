"""
pyramid.py:
    Reads a number of blocks and output the height of the pyramid that
    can be built by these blocks.
"""

if __name__ == '__main__':

    height = int(input('\nEnter the height of the pyramid: '))
    calc_blocks = height

    while height >= 1:
        calc_blocks = calc_blocks + (height - 1)
        height -= 1

    print(f'Total number of blocks needed: {calc_blocks}\n')

    blocks = int(input('Enter the number of blocks: '))
    calc_height = 0

    while blocks > 0:
        blocks -= (calc_height + 2)
        calc_height += 1

    print(f'The height of the piramid is: {calc_height}\n')
