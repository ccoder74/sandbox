"""
fib.py:
    Fibonacci numbers
    f0 = 0
    f1 = 1
    fn = f(n-1)+f(n-2)
"""


def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    fn1 = fn2 = 1
    fn = 0

    for i in range(3, n + 1):
        fn = fn1 + fn2
        fn1, fn2 = fn2, fn

    return fn


if __name__ == '__main__':
    print()
    num = int(input('Enter a positive integer: '))

    print()

    for n in range(1, num):
        print(n, '->', fib(n))

    print()
