#-----------------------------------------------------------------------------
# Name:        Factorial Calculator
# Purpose:     To calculate the factorial of a number inputted by the user
#
# Author:      Sohum Padhye
# Created:     20-Feb-2025
# Updated:     20-Feb-2025
#-----------------------------------------------------------------------------

# take input from user
number = int(input())

# check if the number is invalid
if number < 0:
    print("Error.")
# number is valid, calculate the factorial
else:
    # declare variables to be used to calculate the factorial
    result = 1
    current = number

    while (current > 0):
        # keep multiplying the result by current and update current
        result *= current
        current -= 1
    print(result)