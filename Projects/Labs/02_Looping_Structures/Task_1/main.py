#-----------------------------------------------------------------------------
# Name:        Factorial Calculator
# Purpose:     To calculate the factorial of a number inputted by the user
#
# Author:      Sohum Padhye
# Created:     20-Feb-2025
# Updated:     20-Feb-2025
#-----------------------------------------------------------------------------

number = int(input())

result = 1
current = number

if number < 0:
    print("Error.")
else:
    while (current > 0):
        result *= current
        current -= 1
    print(result)