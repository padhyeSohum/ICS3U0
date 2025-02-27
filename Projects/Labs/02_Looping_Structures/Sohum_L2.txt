#-----------------------------------------------------------------------------
# Name:        Factorial Calculator + Number Adder
# Purpose:     To calculate the factorial of a number inputted by the user, and to determine the sum of a range of numbers inputted by the user
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