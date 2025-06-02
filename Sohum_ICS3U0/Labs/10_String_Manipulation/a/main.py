#-----------------------------------------------------------------------------
# Name:        Conversion Calculator
# Purpose:     To use functions to convert a user-inputted number of units into another unit
#
# Author:      Sohum Padhye
# Created:     7-May-2025
# Updated:     9-May-2025
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

    if not isinstance(celsius, (int, float)):
        raise TypeError("Function expecting integer or float as input for 'celsius'.")
    if celsius < -273:
        raise ValueError("Input value of 'celsius' outside of expected input range (-273, +infinity).")
    
    fahrenheit = celsius*9/5 + 32

    if not isinstance(fahrenheit, (int, float)):
        raise Exception("Celsius not converted to fahrenheit value as expected.")

    return fahrenheit

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

    if not isinstance(miles, (int, float)):
        raise TypeError("Function expecting integer or float as input for 'miles'.")
    if miles < 0:
        raise ValueError("Input value of 'miles' outside of expected input range (0, +infinity).")

    kilometres = miles * 1.60934

    if not isinstance(kilometres, (int, float)):
        raise Exception("Miles not converted to kilometres value as expected.")

    return kilometres

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

    if not isinstance(hours, int):
        raise TypeError("Function expecting integer as input for 'hours'.")
    if not isinstance(minutes, (int, float)):
        raise TypeError("Function exepcting integer or float as input for 'minutes'.")
    if hours < 0:
        raise ValueError("Input value of 'hours' outside of expected input range (0, +infinity).")
    if minutes < 0 or minutes >= 60:
        raise ValueError("Input value of 'minutes' outside of expected input range (0, 60).")
    
    total_minutes = hours*60 + minutes

    if not isinstance(total_minutes, (int, float)):
        raise Exception("Hours and minutes not converted to minutes value as expected.")

    return total_minutes

try:
    print(f"671 degrees Celsius is {celsius_to_fahrenheit(671):,.2f} degrees Fahrenheit")
    # print(celsius_to_fahrenheit('hi'))
    # print(celsius_to_fahrenheit(-280))

    print(f"250586726.6852 miles is {miles_to_kilometers(250586726.6852):,.2f} kilometres.")
    # print(miles_to_kilometers('hi'))
    # print(miles_to_kilometers(-0.5))

    print(f"{time_to_minutes(10, 20):,.2f}")
    # print(time_to_minutes('fjkdls', 0))
    # print(time_to_minutes(10, 'fjdksl'))
    # print(time_to_minutes(-2, 10))
    # print(time_to_minutes(0, 70))

except Exception as e:
    print("Something went wrong:", e)