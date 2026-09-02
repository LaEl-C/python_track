"""Print Exact Greeting
Tests passed ✓
Next challenge
Instructions
Write a function called `solution` that receives a student's name and returns an exact greeting.

The greeting must follow this exact format:

Hello, <name>. Welcome to Talent Nation.

Rules:
- Use the name passed into the function.
- Return the final string.
- Do not print.
- Do not hardcode only the sample names.
"""

def solution(name):
    return f"Hello, {name}. Welcome to Talent Nation."


"""Use Function Input
Tests passed ✓
Next challenge
Instructions
Write a function called `solution` that receives a student's name and learning track, then returns a short profile sentence.

The sentence must follow this exact format:

<name> is starting the <track> track.

Rules:
- Use both function arguments.
- Return the final string.
- Do not print.
- The output must match exactly."""

def solution(name, track):
    return f"{name} is starting the {track} track."

"""Format Multi-line Output
Tests passed ✓
Next challenge
Instructions
Write a function called `solution` that receives a student's name and cohort, then returns a three-line badge.

The badge must follow this exact format:

Name: <name>
Cohort: <cohort>
Status: Ready

Rules:
- Use newline characters between the lines.
- Do not add extra spaces.
- Do not add an extra blank line at the end.
- Return the final string."""

def solution(name, cohort):
    return f"Name: {name}\nCohort: {cohort}\nStatus: Ready"

"""Arithmetic Report
Tests passed ✓
Instructions
Write a function called `solution` that receives a student's name and three numbers.

Return a four-line report in this exact format:

Student: <name>
Sum: <sum>
Average: <average>
Maximum: <maximum>

Rules:
- Add the three numbers to get the sum.
- Divide the sum by 3 to get the average.
- Round the average to 2 decimal places.
- Find the largest number.
- Return the final multi-line string.
- Do not print."""

def solution(name, a, b, c):
    s = (a + b + c)
    ave = round(s/3, 2)
    maxi = max(a, b, c)

    return f"Student: {name}\nSum: {s}\nAverage: {ave}\nMaximum: {maxi}"

"""Convert Length
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
- Do not ask for input."""

def solution(meters):
    meters = float(meters)
    centimeters = 100 * meters
    millimeters = 1000 * meters
    
    return f"Centimeters: {centimeters}\nMillimeters: {millimeters}"

"""Convert Weight
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
    grams = 1000 * kilograms
    pounds = round(kilograms * 2.20462, 2)

    return f"Kilograms: {kilograms}\nGrams: {grams}\nPounds: {pounds}"

"""Reject Bad Input
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
        value = round(float(value) * 2, 2)
        return value

    except ValueError:
        return "Invalid number"

#OR

def solution(value):
    try:
        number = float(value)
        doubled = number * 2
        return round(doubled, 2)
    except ValueError:
        return "Invalid number"

#OR

def solution(value):
    try:
        return round(float(value) * 2, 2)
    except ValueError:
        return "Invalid number"