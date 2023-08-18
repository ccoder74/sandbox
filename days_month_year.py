"""
days_month_year.py
    takes two arguments (a year and a month) from user input and returns
    the number of days for the given month/year pair.
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


def days_in_month(year, month):
    if (month == 1 or month == 3 or month == 5
            or month == 7 or month == 8 or month == 10
            or month == 12):
        return int(31)
    elif (month == 4 or month == 6 or month == 9
            or month == 11):
        return int(30)
    elif month == 2:
        if is_year_leap(year):
            return int(29)
        else:
            return int(28)
    else:
        return None


if __name__ == '__main__':
    year = int(input('\nEnter a year: '))

    if year < 1582:
        print('Not within the Gregorian calender period.\n')
    else:
        month = int(input('Enter a month (1-12): '))
        if days_in_month(year, month) is not None:
            print(f'Month {month} of {year} has ', end='')
            print(f'{days_in_month(year, month)} days.\n')
        else:
            print('The entered month number is not in range 1-12.\n')
