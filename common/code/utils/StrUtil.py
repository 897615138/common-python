# Author Jill
# Date 2021/3/8

import string

"""倒置"""


def reverse(text):
    return text[::-1]


"""回文"""


def is_palindrome(text):
    return text == reverse(text)


"""忽略大小写，空格，标点符号"""


def ignore_space_case_punctuation(text):
    text = ignore_case(text)
    text = ignore_space(text)
    text = ignore_punctuation(text)
    return text


"""忽略大小写"""


def ignore_case(text):
    text = text.lower()
    return text


"""忽略空格"""


def ignore_space(text):
    text = text.replace(' ', '')
    return text


"""忽略标点符号"""


def ignore_punctuation(text):
    for char in string.punctuation:
        text = text.replace(char, '')
    return text
