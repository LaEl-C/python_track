# The Problem:
# Create a program that asks the user to create a password. The program should check if the password meets the following security criteria:

# Length: At least 8 characters long.
# Uppercase: Contains at least one uppercase letter (A-Z).
# Lowercase: Contains at least one lowercase letter (a-z).
# Digits: Contains at least one digit (0-9).
# Special Characters: Contains at least one of these special characters: !, @, #, $, %, ^, &, or *.

# The Challenge:
# Your program should check the password against all five criteria.
# If the password is completely valid, print a congratulatory message: "Password is strong! ✅"
# If the password is invalid, your program should tell the user exactly which criteria they failed. For example: "Your password is missing: uppercase letter, special character."

# Bonus Challenge: Give the user 3 attempts to create a strong password. If they fail after 3 attempts, tell them they have been locked out.


#Creating 5 false variables
length = False
uppercase = False
lowercase = False
digit = False
special_char = False
#Take input password
pass_word = input("Enter Password: ") 

# A loop to check each character against the conditions and change the boolean values to true if any occurence is found
length = True if len(pass_word) >= 8 else False
special_characters = ["!", "@", "#", "$", "%", "^", "&", "*"]
#[!, @, #, $, %, ^, &, *.]
for ch in pass_word:
    ch.isupper() and (uppercase := True)
    ch.islower() and (lowercase := True)
    ch.isdigit() and (digit := True)
    ch in special_characters and (special_char := True)
# A conditional statement that will create message for each condition checked as variables to be later appeneded to result
result_string = []
length_error_message = "" if length else result_string.append(" more characters ")
uppercase_error_message = "" if uppercase else result_string.append(" uppercase letter ")
lowercase_error_message = "" if lowercase else result_string.append("lowercase letter ")
digit_error_message = "" if digit else result_string.append(" digit ")
spe_error_message = "" if special_char else result_string.append(" special character")
result = ",".join(result_string)

if length and uppercase and lowercase and digit and special_char:
    print("Valid password")
else:
    print(f"Your password is missing: {result} . ")



    # print(f"Your password is missing: {lowercase_error_message}{"," if len(lowercase_error_message) != 0 else "" }{uppercase_error_message}{"," if len(uppercase_error_message) != 0 else "" }{length_error_message}{"," if len(length_error_message) != 0 else "" }{digit_error_message}{"," if len(digit_error_message) != 0 else "" }  {spe_error_message}{"," if len(spe_error_message) != 0 else "." }                                                           " )