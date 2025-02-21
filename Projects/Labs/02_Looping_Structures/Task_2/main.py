#-----------------------------------------------------------------------------
# Name:        Number Adder
# Purpose:     To determine the sum of a range of numbers inputted by the user
#
# Author:      Sohum Padhye
# Created:     20-Feb-2025
# Updated:     20-Feb-2025
#-----------------------------------------------------------------------------

# take input from user on range of numbers to be added
begin = int(input())
end = int(input())

# check if input is invalid
if begin > end:
    print("Error.")
# input is valid
else:
    # set the sum to zero
    sum = 0

    # keep adding each number to the sum
    for i in range(begin, end+1):
        sum += i
    print(sum)