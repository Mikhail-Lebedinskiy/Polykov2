from itertools import product

def f(A):
    d = ""
    for i in A:
        d += i
    return d


A = list(product("ПАРУС", repeat=5))
A.sort()
for i in range(len(A)):
    gg = f(A[i])
    if gg[0] == "У" and "АА" not in gg:
        print(i + 1)
        break


