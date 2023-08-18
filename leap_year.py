"""
leap_year.py
    - if the year number < 1582: not within Gregorian calender period;
    - if the year number isn't divisible by four, it's a common year;
    - otherwise, if the year number isn't divisible by 100, it's a leap year;
    - otherwise, if the year number isn't divisible by 400, it's a common year;
    - otherwise, it's a leap year.

"""


def is_year_leap(year):
    if year % 4 != 0:
        return False
    else:
        if year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True


if __name__ == '__main__':
    year = int(input('\nEnter a year: '))

    if year < 1582:
        print('Not within the Gregorian calender period.\n')
    else:
        if is_year_leap(year):
            print(f'{year} is a leap year.')
        else:
            print(f'{year} is a common year.')
    print()
