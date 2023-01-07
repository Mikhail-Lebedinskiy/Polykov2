# 1 способ
from math import gcd


def coprime2(a, b):
    return gcd(a, b) == 1


def f(x1, x2, count_of_commands=5, itog_pars=None):
    if itog_pars is None:
        itog_pars = set()
    if count_of_commands == 0:
        if (min(x1, x2), max(x1, x2)) not in itog_pars and coprime2(x1, x2):
            itog_pars.add((min(x1, x2), max(x1, x2)))
            return 1
        return 0
    return f(x1 + 3, x2, count_of_commands - 1, itog_pars) + \
           f(x1 * 4, x2, count_of_commands - 1, itog_pars) + \
           f(x1, x2 + 5, count_of_commands - 1, itog_pars) + \
           f(x1, x2 * 2, count_of_commands - 1, itog_pars)


print(f(2, 3))

