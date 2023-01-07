from itertools import product


def f(a):
    s = ''
    for i in a:
        s += i
    return s



a = list(product("ПАРУС", repeat = 5))
print(a)
a.sort()
for i in range(len(a)):
    i_str = f(a[i])
    if i_str[0] == "У" and not "АА" in i_str:
        print(i + 1)
        break
