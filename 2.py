from itertools import product, compress
from math import prod
from termcolor import cprint


def NOD(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_good(k, n):
    for i in range(1, k // 2 + 1):
        if NOD(i, n) == 1 == NOD(k - i, n):
            return True
    return False


prime_numbers = [5, 7, 11, 13, 17, 19]

for mask in product([0, 1], repeat=len(prime_numbers)):
    n_prime_numbers = list(compress(prime_numbers, mask))
    n = prod(n_prime_numbers)
    for k in range(2, 2 * n):
        if not is_good(k, n):
            cprint(f'{n_prime_numbers}  {n}  {k} ', color='red')
            break
    else:
        cprint(f'{n_prime_numbers}  {n}', color='green')


print(NOD(1, 4564123))