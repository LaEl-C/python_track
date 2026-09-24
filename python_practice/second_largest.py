# def sec_large(num):
#     maxi1 = num[0]
#     maxi2 = None

#     for ch in num:
#         if ch > maxi1:
#             maxi2 = maxi1
#             maxi1 = ch
#         elif ch != maxi1:
#             if maxi2 is None or ch > maxi2:
#                 maxi2 = ch
#     return maxi2


# print(sec_large([5,4,6,7,3,9,3,7,8]))


def seco_lar(num):
    num.remove(max(num))
    largest = num[0]
    for ch in num:
        if ch > largest:
            largest = ch
    return largest

print(seco_lar([3,5,7,3,6,4,6]))