"""Convert Temperature
Tests passed ✓
Next challenge
Instructions
Write a function called `solution` that converts a Celsius temperature to Fahrenheit.

The function receives one value, `celsius`, and must return the Fahrenheit value rounded to 2 decimal places.

Formula:

fahrenheit = (celsius * 9 / 5) + 32

Rules:
- Convert the input to a number using `float()`.
- Return the converted value.
- Round the answer to 2 decimal places.
- Do not print.
- Do not ask for input."""

def solution(celsius):
    celsius = float(celsius)
    fahrenheit = round((celsius * 9/5) + 32, 2)
    return fahrenheit

#OR

def solution(celsius):
    celsius = float(celsius)
    fahrenheit = (celsius * 9 / 5) + 32
    return round(fahrenheit, 2)


"""Convert Length
Tests passed ✓
Next challenge
Instructions
Write a function called `solution` that converts meters to centimeters and millimeters.

The function receives one value, `meters`, and must return a two-line report in this exact format:

Centimeters: <centimeters>
Millimeters: <millimeters>

Rules:
- Convert the input to a number using `float()`.
- 1 meter = 100 centimeters.
- 1 meter = 1000 millimeters.
- Return the final multi-line string.
- Do not print.
- Do not ask for input.
"""
def solution(meters):
    meters = float(meters)
    centimeters = meters * 100
    millimeters = meters * 1000
    return f"Centimeters: {centimeters}\nMillimeters: {millimeters}"

"""Convert Weight
Tests passed ✓
Next challenge
Instructions
Write a function called `solution` that converts kilograms to grams and pounds.

The function receives one value, `kilograms`, and must return a three-line report in this exact format:

Kilograms: <kilograms>
Grams: <grams>
Pounds: <pounds>

Rules:
- Convert the input to a number using `float()`.
- 1 kilogram = 1000 grams.
- 1 kilogram = 2.20462 pounds.
- Round pounds to 2 decimal places.
- Return the final multi-line string.
- Do not print."""

def solution(kilograms):
    kilograms = float(kilograms)
    grams = kilograms * 1000
    pounds = round(kilograms * 2.20462, 2)
    return f"Kilograms: {kilograms}\nGrams: {grams}\nPounds: {pounds}"

"""Reject Bad Input
Tests passed ✓
Instructions
Write a function called `solution` that safely converts a value to a number and doubles it.

If the value can be converted to a number, return the doubled value rounded to 2 decimal places.

If the value cannot be converted to a number, return this exact string:

Invalid number

Rules:
- Use `float()` inside a `try` block.
- Use `except ValueError` to catch bad input.
- Return "Invalid number" for bad input.
- Do not print.
- Do not ask for input.

This challenge matches the Day 2 safe parsing idea: ask, attempt to convert, handle failure, and continue without crashing."""

def solution(value):
    try:
        return round(float(value) * 2, 2)
    except ValueError:
        return "Invalid number"