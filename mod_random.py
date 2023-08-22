"""
mod_random.py:
    A random number generator takes a value called a seed, treats it as an
    input value, calculates a "random" number based on it (the method depends
    on a chosen algorithm) and produces a new seed value. 

    The length of a cycle in which all seed values are unique may be very long,
    but it isn't infinite. Sooner or later the seed values will start repeating,
    and the generating values will repeat, too. This is normal. It's a feature,
    not a mistake, or a bug.

    The initial seed value, set during the program start, determines the order
    in which the generated values will appear. The random factor of the process
    may be augmented by setting the seed with a number taken from the current
    time - this may ensure that each program launch will start from a different
    seed value (ergo, it will use different random numbers).
"""


from random import choice, randint, random, randrange, sample, seed


if __name__ == '__main__':
    num = int(input('\nEnter number of desired random values: '))

    # random()
    print('\nrandom():')

    for i in range(num):
        print(random())

    # The seed() function is able to directly set the generator's seed.
    # seed() - sets the seed with the current time.
    print('\nrandom() with seed():')
    seed()

    for i in range(num):
        print(random())

    # seed(int_value) - sets the seed with the integer value int_value.
    print('\nrandom() with seed(0):')

    seed(0)

    for i in range(num):
        print(random())

    # randrange(10)
    print('\nrandrange(10):')
    for i in range(num):
        print(randrange(10), end=' ')

    # randrange(10, 20)
    print('\n')
    print('randrange(10, 20):')
    for i in range(num):
        print(randrange(10, 20), end=' ')

    # randrange(10, 20, 20)
    print('\n')
    print('randrange(10, 20, 20):')
    for i in range(num):
        print(randrange(10, 20, 20), end=' ')

    # randint
    print('\n')
    print('randint(num):')
    for i in range(num):
        print(randint(1, num), end=' ')

    # choice(nums09)
    print('\n')
    print('choice(nums09):')

    nums09 = [i for i in range(10)]

    for i in range(num):
        print(choice(nums09), end=' ')

    # sample(nums09, num)
    print('\n')
    print('sample(nums09, num):')
    print(sample(nums09, num), '\n')
