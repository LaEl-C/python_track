"""ReceiptFormatter
Tests passed ✓
Next challenge
Instructions
Implement receipt_formatter(name, quantity, price). Calculate subtotal as quantity multiplied by price. Calculate tax as 7.5 percent of subtotal. Calculate total as subtotal plus tax. Return a four-line report with labels Customer, Subtotal, Tax, and Total. Round subtotal, tax, and total to 2 decimal places."""

def receipt_formatter(name, quantity, price):
    quantity = float(quantity)
    price = float(price)
    subtotal = round(quantity * price, 2)
    tax = round(7.5/100 * subtotal, 2)
    total = round(subtotal + tax, 2)
    return f"Customer: {name}\nSubtotal: {subtotal}\nTax: {tax}\nTotal: {total}"

"""SmartTemperature
Tests passed ✓
Next challenge
Instructions
Implement smart_temperature(value). Convert value to a Celsius number. If conversion fails, return Invalid temperature. Convert Celsius to Fahrenheit using the standard formula. Return a three-line report with labels Celsius, Fahrenheit, and Status. Status is freezing when Celsius is less than or equal to 0, cold when below 20, warm when from 20 through 30, and hot when above 30."""

def smart_temperature(value):
    try:
        celsius = float(value)
    except:
        return "Invalid temperature"
    
    fahrenheit = (celsius * 9/5) + 32
    if celsius <= 0:
        status = "freezing"
    if celsius > 0 and celsius < 20:
        status = "cold"
    if celsius >= 20 and celsius <= 30:
        status = "warm"
    if celsius > 30:
        status = "hot"
    
    return f'Celsius: {celsius}\nFahrenheit: {fahrenheit}\nStatus: {status}'

"""SlugMaker
Tests passed ✓
Next challenge
Instructions
Implement slug_maker(title). Remove leading and trailing spaces, convert the text to lowercase, remove commas and periods, and replace spaces with hyphens. Return the final slug."""

def slug_maker(title):
    return title.strip().lower().replace(",", "").replace(".", "").replace(" ", "-")


"""ManualPalindrome
Instructions
Implement manual_palindrome(text). Ignore spaces and letter case. Return true if the cleaned text reads the same forward and backward, otherwise return false. Do not use slicing shorthand or reversed. Students may need to research manual string reversal."""


def manual_palindrome(text):
    cleaned = text.replace(" ", "").lower()

    reversed_text = ""

    for char in cleaned:
        reversed_text = char + reversed_text

    return cleaned == reversed_text

#OR

def man_pal(text):
    cleaned_text = text.replace(" ", "").lower()

    textb = ""
    for ch in reversed(cleaned_text):
        textb += ch
    # print(textb)
    print(True) if cleaned_text == textb else print(False)

man_pal("madam")
man_pal("Davidevi")




"""ExactCalculator
Instructions
Implement exact_calculator(left, operator, right). Convert left and right to numbers. Support addition, subtraction, multiplication, division, remainder, and exponent. If either number cannot be converted, return Invalid number. If the operator is not supported, return Invalid operator. If division or remainder uses zero on the right side, return Cannot divide by zero. Round numeric results to 2 decimal places."""

def exact_calculator(left, operator, right):
    #convert to float
    try:
        left = float(left)
        right = float(right)
    except:
        return "Invalid number"

    #declare valid operators
    valid_operators = ["+", "-", "*", "/", "%", "**"]

    #handle invalid inputs
    if operator not in valid_operators:
        return "Invalid operator" 

    #calculations using cases
    match operator:
        case "+":
            result = left + right
        case "-":
            result = left - right
        case "*":
            result = left * right
        
        #zerodivisionerror
        case "/":
            try:
                result = left / right
            except ZeroDivisionError:
                return "Cannot divide by zero"
        case "%":
            try:
                result = left % right
            except ZeroDivisionError:
                return "Cannot divide by zero"
        case "**":
            result = left ** right
   
    #round result
    return round(result, 2)


"""InitialsBadge
Tests passed ✓
Next challenge
Instructions
Implement initials_badge(full_name). Remove leading and trailing spaces, split the name into words, take the first character of each word, convert each initial to uppercase, and return the initials joined with dots. The returned badge should end with a dot."""

def initials_badge(full_name):
    #strip and split
    res = full_name.strip().title().split()
    initials = []
    for name in res:
        initials.append(name[0])
    res = ".".join(initials) + "."
    return res

#Or we can use list comprehension

def initials_badge(full_name):
    # Remove leading and trailing spaces
    full_name = full_name.strip()
    
    # Split the name into words
    words = full_name.split()
    
    # Take first character of each word, convert to uppercase
    initials = [word[0].upper() for word in words]
    
    # Join initials with dots and add a trailing dot
    return ".".join(initials) + "."

#Or you can use append

def initials_badge(full_name):
    words = full_name.strip().split()

    initials = ""

    for word in words:
        initials += word[0].upper() + "."
    return initials

# Or for lack of stress

def initials_badge(full_name):
    words = full_name.strip().split()
    return ".".join(word[0].upper() for word in words) + "."


"""ErrorHint
Instructions
Implement error_hint(error_type). Return a helpful debugging hint for common Python errors. For NameError return Check variable names and spelling. For TypeError return Check the types before using an operator. For ValueError return Check whether the value can be converted. For ZeroDivisionError return Check that the denominator is not zero. For IndexError return Check the index is inside the valid range. For anything else return Read the traceback carefully."""


def error_hint(error_type):
    if error_type == "NameError":
        return "Check variable names and spelling."
    elif error_type == "TypeError":
        return "Check the types before using an operator."
    elif error_type == "ValueError":
        return "Check whether the value can be converted."
    elif error_type == "ZeroDivisionError":
        return "Check that the denominator is not zero."
    elif error_type == "IndexError":
        return "Check the index is inside the valid range."
    else:
        return "Read the traceback carefully."



"""ScoreSummary
Instructions
Implement score_summary(name, a, b, c). Convert the three score values to numbers. If conversion fails, return Invalid score. If any score is below 0 or above 100, return Invalid score. Otherwise calculate the average, round it to 2 decimal places, choose a grade, and return a three-line report with labels Student, Average, and Grade. Grade is A for 90 and above, B for 80 and above, C for 70 and above, and F below 70."""

def score_summary(name, a, b, c):
    #convert to float
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except ValueError:
        return "Invalid score"
    #state invalids
    if a < 0 or a > 100 or b < 0 or b > 100 or c < 0 or c > 100:
        return "Invalid score"

    """ if any(score < 0 or score > 100 for score in [a, b, c]):
    return "Invalid score" """
#This could work also

    #calculate and round average
    ave = round((a+b+c)/3, 2)

    #Define grades
    if ave >= 90:
        grade = "A"
    elif ave >= 80:
        grade = "B"
    elif ave >= 70:
        grade = "C"
    else:
        grade = "F"
    #return report
    return f"Student: {name}\nAverage: {ave}\nGrade: {grade}"
