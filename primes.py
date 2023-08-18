"""
primes.py:
    calculate:
    - prime numbers
    - if a user input number is a prime number
"""


def is_prime(up_lim):
    for i in range(2, up_lim):
        if (up_lim % i) == 0:
            return False

    return True


if __name__ == '__main__':

    up_lim = int(input('\nEnter upper limit of primes to find: '))

    for i in range(1, up_lim):
        if is_prime(i + 1):
            print(i + 1, end=' ')

    print('\n')
