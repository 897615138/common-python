#!/usr/bin/python
# Filename: seq.py

shop_list = ['apple', 'mango', 'carrot', 'banana']
name = 'swoop'

# Indexing or 'Subscription' operation
print('Item 0 is', shop_list[0])
print('Item 1 is', shop_list[1])
print('Item 2 is', shop_list[2])
print('Item 3 is', shop_list[3])
print('Item -1 is', shop_list[-1])
print('Item -2 is', shop_list[-2])
print('Character 0 is', name[0])

# Slicing on a list
print('Item 1 to 3 is', shop_list[1:3])
print('Item 2 to end is', shop_list[2:])
print('Item 1 to -1 is', shop_list[1:-1])
print('Item start to end is', shop_list[:])

# Slicing on a string
print('characters 1 to 3 is', name[1:3])
print('characters 2 to end is', name[2:])
print('characters 1 to -1 is', name[1:-1])
print('characters start to end is', name[:])
input()
