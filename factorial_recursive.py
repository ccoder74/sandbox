"""
factorial_recursive.py:
    n! = 1 * 2 * 3 * 4 * ... * n-1 * n
"""


def factorial_recursive(n):
    if n < 0:
        return None
    if n < 2:
        return 1

    return n * factorial_recursive(n - 1)


if __name__ == '__main__':
    n = int(input('\nEnter a positive integer: '))

    print()
    for n in range(1, n + 1):
        print(f'{n}! = {factorial_recursive(n)}')
    print()
