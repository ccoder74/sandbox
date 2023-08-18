"""
collatz.py:
    1. Enter any positive integer and name it c0.
    2. If c0 is even then c0 = c0 // 2
    3. otherwise, if it's odd then c0 = 3 * c0 + 1;
    4. if c0 != 1, skip to point 2.
"""

if __name__ == '__main__':
    c0 = int(input('\nEnter positive integer: '))

    step = 0

    while c0 != 1:
        if c0 % 2 == 0:
            c0 //= 2
        else:
            c0 = 3 * c0 + 1
        step += 1
        print(f'step {step}: c0 = {c0}')
    print()
