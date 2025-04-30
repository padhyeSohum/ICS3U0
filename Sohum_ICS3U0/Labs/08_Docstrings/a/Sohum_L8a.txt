#-----------------------------------------------------------------------------
# Name:        Conversion Calculator
# Purpose:     To use functions to convert a user-inputted number of units into another unit
#
# Author:      Sohum Padhye
# Created:     28-Apr-2025
# Updated:     29-Apr-2025
#-----------------------------------------------------------------------------

# convert temperature from Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    '''
    Converts an inputted temperature of Celsius to Fahrenheit

    Takes a Celsius temperature as input, then performs mathematical operations on
    the inputted temperature to return an equivalent temperature value in Fahrenheit.

    Parameters
    ----------
    celsius : float
        The temperature value in Celsius

    Returns
    -------
    float
        The equivalent value of the inputted temperature in Celsius, in Fahrenheit
    '''

    return celsius*9/5 + 32

# convert distance from miles to kilometres
def miles_to_kilometers(miles):
    '''
    Converts an inputted distance of miles to kilometres

    Takes a miles distance as input, then performs mathematical operations on
    the inputted distance to return an equivalent distance value in kilometres.

    Parameters
    ----------
    miles : float
        The distance value in miles

    Returns
    -------
    float
        The equivalent value of the inputted distance in miles, in kilometres
    '''

    return miles * 1.60934

# convert time from hours and minutes to minutes
def time_to_minutes(hours, minutes):
    '''
    Converts an inputted time of hours and minutes to minutes

    Takes hours and minutes values as input, then performs mathematical operations on
    the inputted values to return an equivalent time value in minutes.

    Parameters
    ----------
    hours : int
        The number of whole hours passed
    minutes: int
        The number of extra minutes after the hour

    Returns
    -------
    int
        The equivalent value of the inputted hours and minutes, in minutes
    '''

    return hours*60 + minutes

# get input of Celsius value and output corresponding Fahrenheit value
celsius = input("Input celsius value: ")
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}C is equal to {fahrenheit}F")

# get input of miles value and output corresponding kilometres value 
miles = input("Input miles value: ")
km = miles_to_kilometers(miles)
print(f"{miles} miles is equal to {km} kilometers")

# get input of hours and minutes value and output corresponding total minutes value
hours = input("Input hours value: ")
minutes = input("Input minutes value: ")
total_minutes = time_to_minutes(hours, minutes)
print(f"{hours} hours and {minutes} minutes is equal to {total_minutes} minutes")