from functools import lru_cache 


@lru_cache(None)
def f(cur, end, k):
    if cur > end * 2 ** (4 - k):
        return 0
    if cur == end:
        if k < 4:
            if cur % 2 == 0:
                return f(cur + 1, end, k) + f(cur // 2, end, k + 1) + 1
            else:
                return f(cur + 1, end, k) + 1
        else:
            return f(cur + 1, end, k) + 1
    else:
        if k < 4:
            if cur % 2 == 0:
                return f(cur + 1, end, k) + f(cur // 2, end, k + 1)
            else:
                return f(cur + 1, end, k)
        else:
            return f(cur + 1, end, k)


print(f(10, 20, 0))
