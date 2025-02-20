#-----------------------------------------------------------------------------
# Name:        Grade Range Finder
# Purpose:     To determine how someone is progressing depending on their grade
#
# Author:      Sohum Padhye
# Created:     20-Feb-2025
# Updated:     20-Feb-2025
#-----------------------------------------------------------------------------

grocery_list = []

item_to_add = input()
while item_to_add != "!":
    if item_to_add not in grocery_list:
        grocery_list.append(item_to_add)
    item_to_add = input()

grocery_list.sort()
print(grocery_list)

print(grocery_list[2])
print(grocery_list[-3])

print(grocery_list[3:6])
print(grocery_list[5:2:-1])

grocery_list.pop()

item_to_remove = input()
if item_to_remove in grocery_list:
    grocery_list.remove(item_to_remove)

print(grocery_list)