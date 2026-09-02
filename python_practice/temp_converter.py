"""Problem: 
Write a program that converts temperatures between Celsius, Fahrenheit, and Kelvin.
"""
#Entering unit
print("Welcome to the Temperature Converter!")
unit_from = input('What unit are you converting from? (C/F/K):  ').upper()
#Entering temperature
temp = float(input("Enter the temperature:  " ))
unit_to = input('What unit are you converting to? (C/F/K):  ').upper()

if unit_from == "C" and unit_to == "F":
    result = (temp * 9 / 5) + 32
    result_string = f"{temp}°C is equal to {round(result, 2)}°F"

elif unit_from == "C" and unit_to == "K":
    result = temp + 273.15
    result_string = f"{temp}°C is equal to {round(result, 2)}K"

elif unit_from == "F" and unit_to == "C":
    result = (temp - 32) * 5 / 9
    result_string = f"{temp}°F is equal to {round(result, 2)}°C"

elif unit_from == "F" and unit_to == "K":
    result = (temp - 32) * 5 / 9 + 273.15
    result_string = f"{temp}°F is equal to {round(result, 2)}K"

elif unit_from == "K" and unit_to == "C":
    result = temp - 273.15
    result_string = f"{temp}K is equal to {round(result, 2)}°C"

elif unit_from == "K" and unit_to == "F":
    result = (temp - 273.15 ) * 9 / 5 +32
    result_string = f"{temp}K is equal to {round(result, 2)}°F"

else:
    result_string = "You entered something wrong"


print(result_string)