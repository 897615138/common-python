# -*-- coding: UTF-8 --*-
# !/usr/bin/python
# Filename: list_comprehension.py

list_one = [2, 3, 4]
list_two = [2 * i for i in list_one if i > 2]
print(list_two)
