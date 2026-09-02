# def clean_username(value):
#     return f"{value.strip().lower().replace(' ', '_')}"
# print (clean_username("Ada Lovelace"))




# def brew_cup(drink, size, temperature):
#     print(f"Brewing a {temperature} {size} {drink}...")

# # Call with exact positional alignment
# brew_cup("Latte", "large", "hot")


# # OR


# def brew_cup_(drink, size, temperature):
#     print(f"Brewing a {temperature} {size} {drink}...")

# Every keyword matches a parameter in the def statement
# brew_cup_(drink="Latte", size="large", temperature="hot")





# # Required fields are declared first, optional default fields are placed last
# def process_order(name, drink, size="medium"):
#     print(f"{name} wants a {size} {drink}")

# # Now we can safely omit the optional size argument
# process_order("Alice", "Latte") # Uses the default "medium"
# process_order("Bob", "Espresso", "large") # Overrides the default






# def label(name, drink, size="medium"):
#     print(name + " wants a " + size + " " + drink)

# # Attempt to place a positional argument AFTER a keyword argument
# label(name="Alice", "espresso")





# def test_scope():
#     secret_recipe = "Vanilla Syrup"
#     print(secret_recipe)

# test_scope()
# # Now try to print it outside:
# print(secret_recipe)





# # Global variable (written on the public whiteboard)
# menu_price = 4.50

# def serve_customer(name):
#     # We can read the global variable naturally
#     print(f"Charging {name} ₦{menu_price:.2f} for their latte.")

# serve_customer("Alice")





# menu_price = 4.50  # Global

# def update_price(new_price):
#     menu_price = new_price  # This accidentally creates a LOCAL variable!
#     print(f"Local function variable set to: ₦{menu_price:.2f}")

# update_price(5.00)
# print(f"Global whiteboard price is: ₦{menu_price:.2f}")





# total_sales = 0.0

# def record_sale(amount):
#     global total_sales
#     total_sales = total_sales + amount
#     print(f"Sale recorded: ₦{amount:.2f}")

# record_sale(4.50)





# count = 0
# def increment():
#     global count
#     count = count + 1
#     print(count)

# increment()
# increment()



# global_sales = 0
# def make_drink():
#     local_count = 0  # Born fresh on every function call
#     global global_sales
    
#     local_count = local_count + 1
#     global_sales = global_sales + 1
#     print(f"Local: {local_count}, Global: {global_sales}")

# make_drink()
# make_drink()
# make_drink()
# make_drink()
# make_drink()





# def run_coffee_cart():
#     # Outer parent function's local variable
#     current_order = "Espresso"
    
#     def change_order(new_drink):
#         nonlocal current_order  # Link to the parent function's variable
#         current_order = new_drink
#         print(f"Order updated to: {current_order}")
        
#     change_order("Latte")
#     print(f"Final cart order: {current_order}")

# run_coffee_cart()




def outer():
    x = "original"
    def inner():
        nonlocal x
        x = "modified"
    inner()
    print(x)

outer()