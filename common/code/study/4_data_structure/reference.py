#!/usr/bin/python
# Filename: reference.py

print('Simple Assignment')
shop_list = ['apple', 'mango', 'carrot', 'banana']
my_list = shop_list  # list is just another name pointing to the same object!

del shop_list[0]  # I purchased the first item, so I remove it from the list

print('shop list is', shop_list)
print('list is', my_list)
# notice that both shop list and list both print the same list without
# the 'apple' confirming that they point to the same object

print('Copy by making a full slice')
my_list = shop_list[:]  # make a copy by doing a full slice
del my_list[0]  # remove first item

print('shop list is', shop_list)
print('list is', my_list)
# notice that now the two lists are different

input()
