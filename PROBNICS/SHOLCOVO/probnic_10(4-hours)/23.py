from functools import lru_cache


@lru_cache(None)
def f(cur, end):
    if cur == end:
        return 1
    if cur < end:
        return 0
    return f(cur - 1, end) + f(cur - 3, end) + f(cur // 3, end)


print(f(38, 14) * f(14, 1))