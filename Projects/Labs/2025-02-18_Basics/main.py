#-----------------------------------------------------------------------------
# Name:        Time Planner
# Purpose:     To perform math operations on various inputs from users
#
# Author:      Sohum Padhye
# Created:     18-Feb-2025
# Updated:     18-Sep-2025
#-----------------------------------------------------------------------------

# take the number of hours and divide by seven to get daily study hours
hours_to_study = int(input("How many hours do you want to study this week? "))
hours_to_study_per_day = hours_to_study/7
print(f"You would have to study an average of {hours_to_study_per_day} hours per day to meet this goal, if you studied every day. Make sure this seems realistic and tangible!")

# take the number of hours and floor divide by number of intended study days to get actual number of daily study hours, then add the missing hours in another statement
num_days_studying = int(input("How many days this week do you plan to study? "))
print(f"Then you would be studying for approximately {hours_to_study//num_days_studying} hours per day of study. You would have {hours_to_study%num_days_studying} hours left over. You could allocate this time to an extra study day!")

# take the number of hours and multiply by seven to get total time spent on extracurriculars
ec_commitment_per_day = int(input("How many hours per day do you spend on extracurriculars, on average? "))
ec_commitment = ec_commitment_per_day*7
print(f"That takes a total of {ec_commitment} hours out of your week!")

# take the number of hours and add one to encourage the user to get more sleep
hours_of_sleep_per_day = int(input("How many hours of sleep do you get per day? "))
print(f"That's a good amount, but try aiming for more sleep. Even a small increase of one hour to {hours_of_sleep_per_day + 1} hours of sleep per day can make a big difference.")

# take the number of hours and subtract two to encourage the user to spend less time on their phone
hours_on_phone = int(input("Weekly, how many hours do you spend on your phone? "))
print(f"Okay, try reducing that by one hour this week, and gradually work your way down to make more time for yourself! Start by aiming for only {hours_on_phone - 2} hours on your phone this week.")