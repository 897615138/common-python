#!/usr/bin/python
# Filename: func_doc.py
def print_max(x, y):
    """Prints the maximum of two numbers.

    The two values must be integers."""
    x = int(x)  # convert to integers, if possible
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')


print_max(3, 5)
print(help(print_max))
print(print_max.__doc__)
