"""
list_comprehensions.py:
    A list comprehension is a list created on-the-fly during program
    execution, and is not described statically.
"""

if __name__ == '__main__':
    squares = [x ** 2 for x in range(10)]
    print(f'\nsquares: {squares}')

    twos = [2 ** x for x in range(10)]
    print(f'twos: {twos}')

    cubed = [x ** 3 for x in range(10)]
    print(f'cubed: {cubed}')

    odds = [x for x in squares if x % 2 != 0]
    print(f'odds: {odds}\n')
