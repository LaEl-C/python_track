num = int(input("Enter number: "))
div = []

for ch in range(1, num+1):
    if num % ch == 0:
        div.append(ch)
print(div)




# num = int(input("Enter number: "))
# div = []

# for ch in range(1, (num//2)+1):
#     if num % ch == 0:
#         div.append(ch)
# print(div)


y = range(1,11)
f = []
for x in y:
    f.append(x)
print(f)