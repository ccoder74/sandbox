"""
cmd_line_pars.py:
    parsing command line arguments
"""

import getopt
import sys


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'ho:v', ['help', 'output='])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        print('ERROR\n')
        sys.exit(2)

    output = None
    verbose = False

    for o, a in opts:
        if o == '-v':
            verbose = True
        elif o in ('-h', '--help'):
            print('HELP\n')
            sys.exit()
        elif o in ('-o', '--output'):
            output = a
        else:
            assert False, 'unhandled exception'
    # ...


if __name__ == '__main__':

    print(f'\nArgument count: {len(sys.argv)}\n')

    for i, arg in enumerate(sys.argv):
        print(f'Argument {i:>2}: {arg}')

    print(f'\nNow entering {__name__}\n')

    main()
