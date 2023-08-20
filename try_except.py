"""
try_except.py:
    framework python program
"""

if __name__ == '__main__':
    try:
        value = int(input('\nEnter a natural number: '))
        print('The reciprocal of', value, 'is', 1/value, '\n')
    except ValueError:
        print('I do not know what to do.\n')
    except ZeroDivisionError:
        print('Division by zero is not allowed in our Universe.\n')
    except:
        print('Something strange has happened here... Sorry!\n')
