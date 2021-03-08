#!/usr/bin/python
# Filename: using_list.py

# This is my shopping list
shop_list = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shop_list), 'items to purchase.')

print('These items are:', end=' ')

for item in shop_list:
    print(item, end=' ')

print('\nI also have to buy rice.')
shop_list.append('rice')
print('My shopping list is now', shop_list)

print('I will sort my list now')
shop_list.sort()
print('Sorted shopping list is', shop_list)
print('The first item I will buy is', shop_list[0])
old_item = shop_list[0]
del shop_list[0]
print('I bought the', old_item)
print('My shopping list is now', shop_list)
input()
