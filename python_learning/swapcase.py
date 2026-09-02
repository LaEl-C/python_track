def swap_case(text):
    new_text = ""
    for ch in text:
        if ch.islower():
            new_text += ch.upper()
        elif ch.isupper():
            new_text += ch.lower()
    return new_text

print(swap_case("nyLoRaC"))



def scase(text):
    return text.swapcase()
print(scase("daVid"))



# recursion
def swap_case(text):
    # Base case: empty string
    if not text:
        return ""
    
    # Process the first character
    first_char = text[0]
    if first_char.islower():
        swapped_char = first_char.upper()
    elif first_char.isupper():
        swapped_char = first_char.lower()
    else:
        swapped_char = first_char
    
    # Recursive case: process the rest of the string
    return swapped_char + swap_case(text[1:])

print(swap_case("nyLoRaC"))  # Output: NYlOrAc