"""ArithmeticEngine
Instructions
Implement arithmetic_engine(a, b). Return a dictionary with three keys: "sum", "product", and "power". The sum is a + b, the product is a * b, and the power is a ** b."""

def arithmetic_engine(a, b):
    dictionary = {
        "sum": a + b,
        "product": a * b,
        "power": a ** b
    }
    return dictionary

"""DivisionDetails
Instructions
Implement division_details(a, b). Return a dictionary with three keys: "true_division", "floor_division", and "remainder". true_division should be a / b rounded to 2 decimal places. floor_division should be a // b. remainder should be a % b."""

def division_details(a, b):
    dictionary = {
        "true_division": round(a/b, 2),
        "floor_division": a//b,
        "remainder": a%b
    }
    return dictionary

"""EligibilityLogic
Instructions
Implement eligibility_logic(score, attendance, completed_drill). Return "Eligible" only when score is greater than or equal to 70, attendance is greater than or equal to 80, and completed_drill is True. Otherwise return "Not eligible"."""

def eligibility_logic(score, attendance, completed_drill):
    if score >= 70 and attendance >= 80 and completed_drill == True:
        return "Eligible"
    
    else:
        return "Not eligible"


"""SafeCalculator
Instructions
Implement safe_calculator(a, operator, b). Return the result of applying the operator to the two numbers. Supported operators are "+", "-", "*", "/", "%", and "**". If the operator is unknown, return "Invalid operator". If the operator is "/" or "%" and b is 0, return "Cannot divide by zero". Round division results to 2 decimal places."""

def safe_calculator(a, operator, b):
    match operator:
        case "+":
            result = a + b
        case "-":
            result = a - b
        case "*":
            result = a * b
        case "/":
            if b == 0:
                result = "Cannot divide by zero"
            else:
                result = round(a / b, 2)
        case "%":
            if b == 0:
                result = "Cannot divide by zero"
            else:
                result = round(a % b, 2)
        case "**":
            result = a ** b
        case _:
            result = "Invalid operator"
    return result

#OR

def safe_calculator(a, operator, b):
    # Check if the operator is supported
    if operator not in ["+", "-", "*", "/", "%", "**"]:
        return "Invalid operator"
    
    # Check for division by zero
    if operator in ["/", "%"] and b == 0:
        return "Cannot divide by zero"
    
    # Perform the calculation
    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        result = a / b
    elif operator == "%":
        result = a % b
    elif operator == "**":
        result = a ** b
    
    # Round division results to 2 decimal places
    if operator in ["/", "%"]:
        result = round(result, 2)
    
    return result