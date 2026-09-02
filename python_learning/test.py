selected_drink = "Hot Cocoa"

if selected_drink == "Green Tea":
    target_temp = 80
elif selected_drink == "Coffee":
    target_temp = 90
else:
    target_temp = 100  # Fallback temperature for any other drink

print(target_temp)



customer_name = "  alIce in the wonderland   "

# Clean the string and save the output back into a variable
cleaned_name = customer_name.strip()
proper_name = cleaned_name.capitalize()

print("[" + proper_name + "]")



name = "Christopher"
print(name[0:5])



customer = "Bob"
total = 12.8378
print(f"Thank you, {customer}! Total: ₦{total:.2f}")



# System State:
raw_order_list = "latte,espresso,mocha"
menu_display = ""

# 1. Split the comma-separated string into a List
items = raw_order_list.split(",")
print(items)

# 2. Join the List using a newline character (\n) as the separator
menu_display = "\n".join(items)
print(menu_display)


sentence = "latte + espresso + mocha + garri"
words = sentence.split(" + ")
print(words)
rejoined = "-".join(words).capitalize()
print(rejoined)