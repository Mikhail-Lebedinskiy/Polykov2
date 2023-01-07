def f(n):
    if n < 3:
        return 2 * n
    if n % 2 == 0:
        return 3 * n + 5 + f(n - 2)
    return n + 2 * f(n - 6)


print(f(61))