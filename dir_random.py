"""
dir_random.py:
    dir() is a standard module that returns the names of the module name
    give as is it's parameter in alphabetically sorted list. So dir(random)
    gives the names of the module math in alphabetically sorted order. 
    There is one condition: the module has to have been previously imported
    as a whole.
"""


import random

if __name__ == '__main__':
    print()
    for name in dir(random):
        print(name)
    print()
