def f(i):
    answer = ""
    g = 0
    while i != 0:
        if i % 12 == 0:
            g += 1
        i = i // 12
    return g

i = 15 * (1728**8) + 9 * (144**12) + 7 * (12**12) + 154
s = f(i)

print(s)