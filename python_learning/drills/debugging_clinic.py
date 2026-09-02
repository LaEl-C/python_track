"""FixGreetingBug
Tests passed ✓
Next challenge
Instructions
Implement fix_greeting(name). Return a greeting in this exact format: Hello, Ada. Replace Ada with the provided name. The starter idea contains a common variable-name mistake. Fix the function so it uses the argument correctly."""

def fix_greeting(name):
    # Bug to fix: the function should use name, not an undefined variable.
    return f"Hello, {name}."


"""FixAgeMath
Tests passed ✓
Next challenge
Instructions
Implement next_age(age_text). The function receives age as text. Convert it to an integer and return the age next year. This fixes the common bug where text is used like a number."""

def next_age(age_text):
    # Bug to fix: age_text is text, so convert it before adding.
    return int(age_text) + 1


"""FixSafeDivide
Tests passed ✓
Next challenge
Instructions
Implement safe_divide(a, b). Return a divided by b rounded to 2 decimal places. If b is zero, return Cannot divide by zero. This fixes the common ZeroDivisionError bug."""

def safe_divide(a, b):
    # Bug to fix: dividing by zero crashes the program.
    try:
        return round(a/b, 2)
    except:
        return "Cannot divide by zero"

#OR

def safe_divide(a, b):
    # Bug to fix: dividing by zero crashes the program.
    try:
        return round(a/b, 2)
    except ZeroDivisionError:
        return "Cannot divide by zero"

#OR
def safe_divide(a, b):
    # Bug to fix: dividing by zero crashes the program.
    if b == 0:
        return "Cannot divide by zero"
    return round(a/b, 2)


"""FixIndexLookup
Tests passed ✓
Next challenge
Instructions
Implement get_item(items, index). Return the item at the given index. If the index is outside the list, return Index out of range. Negative indexes should also return Index out of range for this challenge."""

def get_item(items, index):
    # Bug to fix: invalid indexes should not crash the program.
    try:
        return items[index]
    except:
        return "Index out of range"

#the method above is not accepted though. Use this instead

def get_item(items, index):
    # Bug to fix: invalid indexes should not crash the program.
    if index < 0 or index >= len(items):
        return "Index out of range"
    return items[index]


"""FixBrokenGrade
Instructions
Implement grade_label(score). Return A for scores from 90 to 100, B for scores from 80 to 89, C for scores from 70 to 79, and F for scores below 70. If the score is less than 0 or greater than 100, return Invalid score. This fixes common comparison and branch-order bugs.
"""

def grade_label(score):
    # Bug to fix: branch order and boundary checks must be correct.
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90 and score <= 100:
        return "A"
    elif score >=80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    else:
        return "F"