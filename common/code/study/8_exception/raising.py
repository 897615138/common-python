# -*-- coding: UTF-8 --*-
# !/usr/bin/python
# filename: raising.py

class ShortInputException(Exception):
    '''A user-defined exception class'''

    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.at_least = atleast


try:
    text = input('Enter something-->')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
# other work can continue as usual here
except EOFError:
    print('Why did you do an EOF on me')
except ShortInputException as ex:
    print('ShortInputException The input was {0} long, excepted at least {1}'.format(ex.length, ex.at_least))
else:
    print('No exception was raised.')
