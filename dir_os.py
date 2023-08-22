"""
dir_os.py:
    dir() is a standard module that returns the names of the module name
    give as is it's parameter in alphabetically sorted list. So dir(os)
    gives the names of the module math in alphabetically sorted order.
    There is one condition: the module has to have been previously imported
    as a whole.
"""


import os

if __name__ == '__main__':
    print()
    for name in dir(os):
        print(name)
    print()
