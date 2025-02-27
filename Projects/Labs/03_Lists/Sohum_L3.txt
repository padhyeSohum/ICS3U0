#-----------------------------------------------------------------------------
# Name:        Grocery List
# Purpose:     To simulate a grocery list using list operations
#
# Author:      Sohum Padhye
# Created:     20-Feb-2025
# Updated:     20-Feb-2025
#-----------------------------------------------------------------------------

# initialize empty list
grocery_list = []

# take input from user
item_to_add = input()

# while input is a valid item:
while item_to_add != "!":

    # add item if not already added
    if item_to_add not in grocery_list:
        grocery_list.append(item_to_add)

    # take input from user
    item_to_add = input()

# sort and output the list
grocery_list.sort()
print(grocery_list)

# output third and third last items
print(grocery_list[2])
print(grocery_list[-3])

# output 4th to 6th and same thing backwards
print(grocery_list[3:6])
print(grocery_list[5:2:-1])

# remove last item
grocery_list.pop()

# take input from user to remove item
item_to_remove = input()

# only remove if in the list
if item_to_remove in grocery_list:
    grocery_list.remove(item_to_remove)

# output new list
print(grocery_list)