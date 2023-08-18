"""
bmi.py:
    calculates bmi = weight in kg / heigh_in_meters^2
"""


def bmi(w, h):
    if w <= 0 or h <= 0:
        return None
    else:
        return w / (h / 100) ** 2


if __name__ == '__main__':
    weight = float(input('\nEnter your weight (kg): '))
    height = float(input('Enter your height (cm): '))

    if bmi(weight, height) is not None:
        print(f'\nYour bmi is: {bmi(weight, height)}\n')
    else:
        print('\nIncorrect input.\n')
