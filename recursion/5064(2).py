# 2 способ
from math import gcd


A = set()


def coprime2(a, b):
    return gcd(a, b) == 1


def f(x1, x2, count_of_commands=5):
    if count_of_commands == 0:
        if coprime2(x1, x2):
            A.add((min(x1, x2), max(x1, x2)))
        return 0
    return f(x1 + 3, x2, count_of_commands - 1) + \
           f(x1 * 4, x2, count_of_commands - 1) + \
           f(x1, x2 + 5, count_of_commands - 1) + \
           f(x1, x2 * 2, count_of_commands - 1)


f(2, 3)
print(len(A))
