def celsius_to_fahrenheit(celsius):
    return celsius*9/5 + 32

def miles_to_kilometers(miles):
    return miles * 1.60934

def time_to_minutes(hours, minutes):
    return hours*60 + minutes

celsius = input("Input celsius value: ")
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}C is equal to {fahrenheit}F")

miles = input("Input miles value: ")
km = miles_to_kilometers(miles)
print(f"{miles} miles is equal to {km} kilometers")

hours = input("Input hours value: ")
minutes = input("Input minutes value: ")
total_minutes = time_to_minutes(hours, minutes)
print(f"{hours} hours and {minutes} minutes is equal to {total_minutes} minutes")