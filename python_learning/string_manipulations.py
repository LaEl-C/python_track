title = "Menu"
print(title.center(20))
print([title.center(20)])
print("Menu".center(20, "*"))
print("Menu".center(20, "-"))
print("Menu".center(20, "="))


def banner(text, width=40, fill="-"):
    print(text.center(width, fill))
    print("Welcome to the system".center(width))

banner("MENU")

print("Hello WORLD".casefold())

a = "STRASSE"
b = "Straße"
print(a.lower() == b.lower())        # False
print(a.casefold() == b.casefold())  # True


text = "Mary had a little lamb"
print(text.count("a"))

text2 = "the cat sat on the mat, the end"
print(text2.count("the"))



text = "hello"
data = text.encode()
print(data)
print(type(data))

text = "café"
data = text.encode()
print(data)

text = "café"
print(len(text))          # 4  (4 characters)
print(len(text.encode())) # 5  (5 bytes — é is 2 bytes)

print("😀".encode())     # b'\xf0\x9f\x98\x80'
print(len("😀".encode()))  # 4
print(len("😀"))



"hello".endswith("lo")     # True
"hello".endswith("he")     # False