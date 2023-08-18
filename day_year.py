"""
day_year.py
    takes three arguments (year, month, day of the month) from user input
    and returns the number of days for the given month/year pair.
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


def day_of_year(year, month, day):
    total_days = 0

    if is_year_leap(year):
        feb_days = 29
    else:
        feb_days = 28

    match month:

        case 1 | 3 | 5 | 7 | 8 | 10 | 12:

            if not (day >= 1 and day <= 31):
                return None
            else:
                if month == 1:
                    total_days = day
                elif month == 3:
                    total_days = 31 + feb_days + day
                elif month == 5:
                    total_days = 2 * 31 + 30 + feb_days + day
                elif month == 7:
                    total_days = 3 * 31 + 2 * 30 + feb_days + day
                elif month == 8:
                    total_days = 4 * 31 + 2 * 30 + feb_days + day
                elif month == 10:
                    total_days = 5 * 31 + 3 * 30 + feb_days + day
                elif month == 12:
                    total_days = 6 * 31 + 4 * 30 + feb_days + day

        case 4 | 6 | 9 | 11:
            if not (day >= 1 and day <= 30):
                return None
            else:
                if month == 2:
                    total_days = 31 + day
                elif month == 4:
                    total_days = 2 * 31 + feb_days + day
                elif month == 6:
                    total_days = 3 * 31 + 30 + feb_days + day
                elif month == 9:
                    total_days = 5 * 31 + 2 * 30 + feb_days + day
                elif month == 11:
                    total_days = 6 * 31 + 3 * 30 + feb_days + day

        case 2:
            if not (day >= 1 and day <= feb_days):
                return None
            else:
                total_days = 31 + day

    return total_days


if __name__ == '__main__':
    year = int(input('\nEnter a year: '))

    if year < 1582:
        print('Not within the Gregorian calender period.\n')
    else:
        month = int(input('Enter a month (1-12): '))

        if days_in_month(year, month) is not None:
            day = int(input('Enter a day (1-31): '))

            if day_of_year is not None:
                print(f'{year}:{month}:{day}: ', end='')
                print(f'{day_of_year(year, month, day)} days.\n')
            else:
                print('The entered day of the month is not in range', end='')
                print('of the days of the month.\n')
        else:
            print('The entered month number is not in range 1-12.\n')
