#-----------------------------------------------------------------------------
# Name:        Number Adder
# Purpose:     To determine the sum of a range of numbers inputted by the user
#
# Author:      Sohum Padhye
# Created:     20-Feb-2025
# Updated:     20-Feb-2025
#-----------------------------------------------------------------------------

begin = int(input())
end = int(input())

if begin > end:
    print("Error.")
else:
    sum = 0
    for i in range(begin, end+1):
        sum += i
    print(sum)