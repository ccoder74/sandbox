"""
mod_platform.py:
    The platform module lets you access the underlying platform's data,
    i.e., hardware, operating system, and interpreter version information.
"""

from platform import machine, node, platform, processor, python_implementation
from platform import python_version_tuple, system, version


if __name__ == '__main__':
    # platform.platform()
    print('\nplatform(): ', end='')
    print(platform())
    print('\nplatform(aliased=False, terse=False): ', end='')
    print(platform(aliased=False, terse=False))
    print('platform(aliased=False, terse=True): ', end='')
    print(platform(aliased=False, terse=True))
    print('platform(aliased=True, terse=False): ', end='')
    print(platform(aliased=False, terse=True))
    print('platform(aliased=True, terse=True): ', end='')
    print(platform(aliased=True, terse=True))
    print('\nplatform(0, 0): ', end='')
    print(platform(0, 0))
    print('platform(0, 1): ', end='')
    print(platform(0, 1))
    print('platform(1, 0): ', end='')
    print(platform(1, 0))
    print('platform(1, 1): ', end='')
    print(platform(1, 1), '\n')

    # platform.machine()
    print('platform.machine():', machine())

    # platform.node()
    print('platform.node():', node())

    # platform.processor()
    print('platform.processor():', processor())

    # platform.python_implementation()
    print('\nplatform.python_implementation():', python_implementation())

    # platform.python_version_tuple()
    print('\nplatform.python_python_version_tuple():')
    major, minor, patch = python_version_tuple()
    print('major:', major)
    print('minor:', minor)
    print('patch:', patch, '\n')

    # platform.system()
    print('platform.system():', system())

    # platform.version()
    print('platform.version():', version(), '\n')
