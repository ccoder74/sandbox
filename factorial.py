"""
factorial.py:
    n! = 1 * 2 * 3 * 4 * ... * n-1 * n
"""


def factorial(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    product = 1

    for i in range(2, n + 1):
        product *= i

    return product


if __name__ == '__main__':
    n = int(input('\nEnter a positive integer: '))

    print()
    for n in range(1, n + 1):
        print(f'{n}! = {factorial(n)}')
    print()
