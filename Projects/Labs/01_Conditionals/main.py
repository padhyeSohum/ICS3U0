#-----------------------------------------------------------------------------
# Name:        Grade Range Finder
# Purpose:     To determine how someone is progressing depending on their grade
#
# Author:      Sohum Padhye
# Created:     20-Feb-2025
# Updated:     20-Feb-2025
#-----------------------------------------------------------------------------

grade = int(input())

if grade > 100 or grade < 0:
    print("Invalid Grade.")
elif grade >= 80:
    print("Exceeding Expectations.")
elif grade >= 70:
    print("Meeting Expectations.")
elif grade >= 50:
    print("Needs Improvement.")
else:
    print("Not Passing.")