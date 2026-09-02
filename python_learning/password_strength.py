count = 3
while count > 0:
    #take input
    password = input("Enter your password: ")
    # define special character set
    special_char = {"!", "@", "#", "$", "%", "^", "&", "*"}

    u_case= any((char.isupper()) for char in password)
    l_case= any((char.islower()) for char in password)
    d_case= any((char.isdigit()) for char in password)
    s_case= any(char for char in password if char in special_char)


    result = []
    if len(password) >= 8 and u_case and l_case and d_case and s_case:
        print("Password is strong!")

        exit()
    if len(password) < 8:
        result.append("at least 8 characters")
    if not u_case:
        result.append("uppercase letter")
    if not l_case:
        result.append("lowercase letter")
    if not d_case:
        result.append("digit")
    if not s_case:
        result.append("special character")
    result = ", ".join(result)


    print(f"Your password is missing: {result}.")

    count-=1
    print(f"You have {count} tries left!!")
print("NO MORE TRIES!!!")