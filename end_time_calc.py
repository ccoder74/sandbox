"""
end_time_calc.py
    Evaluate the end time of a period of time, given as number of minutes
    (it could be arbitrarily large). The start time is given as a pair of
    hours (0..23) and minutes (00.59). The result has to be printed
    to the console.
"""

if __name__ == '__main__':
    begin_hour = int(input('\nStarting time (hours): '))
    begin_mins = int(input('Starting time (minutes): '))
    duration = int(input('Event duration (minutes): '))

    print('\nStarting time: ' + str(begin_hour) + ':' + str(begin_mins))
    print('Duration: ' + str(duration // 60) + ' hours', end='')
    print(' and ' + str(duration - ((duration // 60) * 60)) + ' minutes.')

    end_mins = (begin_mins + duration) % 60
    end_hour = int(begin_hour + (begin_mins + duration) / 60) % 24

    print('End time: ' + str(end_hour) + ':' + str(end_mins) + '\n')
