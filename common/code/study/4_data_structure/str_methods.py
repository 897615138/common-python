#!/usr/bin/python
# Filename: str_methods.py

name = 'Swoop'  # This is a string object

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
my_list = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(my_list))

input()
