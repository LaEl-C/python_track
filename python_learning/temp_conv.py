"""The Problem:

Write a program that converts temperatures between Celsius, Fahrenheit, and Kelvin.

The user should:

Choose which unit they're converting from (C, F, or K)

Enter the temperature

Choose which unit they're converting to (C, F, or K)

See the converted result



The Conversion Formulas:

Celsius to Fahrenheit: (C × 9/5) + 32

Celsius to Kelvin: C + 273.15

Fahrenheit to Celsius: (F - 32) × 5/9

Fahrenheit to Kelvin: (F - 32) × 5/9 + 273.15

Kelvin to Celsius: K - 273.15

Kelvin to Fahrenheit: (K - 273.15) × 9/5 + 32"""

print("Welcome to the Temperature Converter!")

#Get input
unit_from = input("What unit are you converting from? (C/F/K): ").upper()
temp = input("Enter the temperature: ")
unit_to = input("What unit are you converting to? (C/F/K): ").upper()

# Validate units
valid_units = ["C", "F", "K"]
if unit_from not in valid_units or unit_to not in valid_units:
    print("Invalid unit! Please enter C, F, or K.")
    exit()
    
# Validate empty input
if temp == "":
    print("No temperature entered!")
    exit()

#check integer or float
try:
    temp = float(temp)
except ValueError:
    print("Invalid Entry! Numbers only!")
    exit()

if (unit_from == "C" and temp < -273.15) or (unit_from == "F" and temp < -459.67) or (unit_from == "K" and temp < 0):
    print ("Error: Temperature below absolute zero!")
    exit()

"""absolute_zero = {"C": -273.15, "F": -459.67, "K": 0}
if temp < absolute_zero[unit_from]:
    print("Error: Temperature below absolute zero!")
    exit()
    
    or"""

# Perform conversion (all with consistent formatting)
match (unit_from, unit_to):
    case ("C", "F"):
        res = round((temp * 9/5) + 32, 2)
        print(f"{temp}°C is equal to {res}°F")
    case ("C", "K"):
        res = round(temp + 273.15, 2)
        print(f"{temp}°C is equal to {res}K")
    case ("F", "C"):
        res = round((temp - 32) * 5/9, 2)
        print(f"{temp}°F is equal to {res}°C")
    case ("F", "K"):
        res = round((temp - 32) * 5/9 + 273.15, 2)
        print(f"{temp}°F is equal to {res}K")
    case ("K", "C"):
        res = round(temp - 273.15, 2)
        print(f"{temp}K is equal to {res}°C")
    case ("K", "F"):
        res = round((temp - 273.15) * 9/5 + 32, 2)
        print(f"{temp}K is equal to {res}°F")
    case _:
        print("Sorry! Invalid conversion pair.")
        exit()


