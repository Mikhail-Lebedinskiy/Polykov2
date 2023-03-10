from functools import lru_cache


# @lru_cache(None)
# def f(n):
#     if n <= 0:
#         return 0
#     if 0 < n < 3:
#         return f(n) == 2
#     if n > 2 and n % 2 == 0:
#         return f(n - 1) + f(n - 2) - n
#     if n > 2 and n % 2 == 1:
#         return f(n - 1) - f(n - 2) + 2 * n


def f(n):
    if n < 3:
        return 2
    if n > 2 and n % 2 == 0:
        return f(n - 1) + f(n - 2) - n
    if n > 2 and n % 2 == 1:
        return f(n - 2) - f(n - 1) + 2 * n


print(f(30))
