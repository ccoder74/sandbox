"""
triangle.py:
    the sum of two arbitrary sides has to be longer than the third side.
    user input: three numbers a, b and c
    output:
    - triangle: True if a triangle can be constructed with a, b and c.
                False if no triangle can be constructed with a, b and c
    - right_triangle: True if a, b and c can make a right triangle
                      False if  if a, b and c can't make a right triangle
"""


def is_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def is_right_triangle(a, b, c):
    if not is_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


def heron(a, b, c):
    p = (a + b + c) / 2
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


def area_triangle(a, b, c):
    if not is_triangle(a, b, c):
        return None
    return heron(a, b, c)


if __name__ == '__main__':
    side_a = float(input('\nEnter length a: '))
    side_b = float(input('Enter length b: '))
    side_c = float(input('Enter length c: '))

    print(f'\nTriangle: {is_triangle(side_a, side_b, side_c)}')
    print(f'Right Triangle: {is_right_triangle(side_a, side_b, side_c)}')
    print(f'Area Triangle: {area_triangle(1., 1., 2. ** .5)}\n')
