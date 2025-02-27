#-----------------------------------------------------------------------------
# Name:        Grade Range Finder
# Purpose:     To determine how someone is progressing depending on their grade
#
# Author:      Sohum Padhye
# Created:     20-Feb-2025
# Updated:     20-Feb-2025
#-----------------------------------------------------------------------------

# take input from user
grade = int(input())

# check for invalid grades
if grade > 100 or grade < 0:
    print("Invalid Grade.")
# check if grade is at least 80
elif grade >= 80:
    print("Exceeding Expectations.")
# check if grade is at least 70
elif grade >= 70:
    print("Meeting Expectations.")
# check if grade is at least 50
elif grade >= 50:
    print("Needs Improvement.")
# grade is from 0 to 49 inclusive
else:
    print("Not Passing.")