def two_sums(lit, target):
    res = []
    lit2 = lit[1:]
    for i in lit:
        for j in lit2:
            if i + j == target:
                return [i, j]
    return res


print(two_sums([5,2,7,3,4,8,6], 10))



