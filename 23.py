from functools import lru_cache


@lru_cache(None)
def f(n, itog):
    if n > itog:
        return 0
    if n == itog:
        return 1
    return f(n + 1, itog) + f(n + 2, itog)


print(f(11, 17))
print(f(17, 29))
print(f(17, 23))
print(f(11, 23))
print(f(23, 29))

print(13 * 233 + 233 * 13 - 13 * 13 * 13)

