"""
three_dim_array.py:
    a three-diminesional array (3x3x3)
"""

if __name__ == '__main__':

    cube = [[['x0y0z0', 'x0y0z1', 'x0y0z2'],
             ['x0y1z0', 'x0y1z1', 'x0y1z2'],
             ['x0y2z0', 'x0y2z1', 'x0y2z2']],

            [['x1y0z0', 'x1y0z1', 'x1y0z2'],
             ['x1y1z0', 'x1y1z1', 'x1y1z2'],
             ['x1y2z0', 'x1y2z1', 'x1y2z2']],

            [['x2y0z0', 'x2y0z1', 'x2y0z2'],
             ['x2y1z0', 'x2y1z1', 'x2y1z2'],
             ['x2y2z0', 'x2y2z1', 'x2y2z2']]]

    print(f'\n{cube}', end='')

    for x in range(3):
        print('\n', end='')
        for y in range(3):
            print('\n', end='')
            for z in range(3):
                print(cube[x][y][z], end=' ')

    print('\n')
