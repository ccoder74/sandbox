"""
dict_rgb.py:
    dictionary of rgb valaues
    color: (red-value, green-value, blue-value)
    Range value: 0-255
"""

if __name__ == '__main__':
    colors = {
            'black': (0, 0, 0),
            'blue': (0, 0, 255),
            'cyan': (0, 255, 255),
            'green': (0, 128, 0),
            'grey': (128, 128, 128),
            'lime': (0, 255, 0),
            'magenta': (255, 0, 255),
            'maroon': (128, 0, 0),
            'navy': (0, 0, 128),
            'olive': (128, 128, 0),
            'purple': (128, 0, 128),
            'teal': (0, 128, 128),
            'red': (255, 0, 0),
            'silver': (192, 192, 192),
            'white': (255, 255, 255),
            'yellow': (255, 255, 0)
            }


print()

for col, rgb in colors.items():
    print(col, ':', rgb)

print()
