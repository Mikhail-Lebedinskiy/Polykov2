from functools import lru_cache


@lru_cache(None)
def f(curr: int, end: int) -> int:
    if curr == end:
        return 1
    if curr > end:
        return 0
    v1 = curr % 10 == 0
    v2 = curr < 20
    max_r = max(int(i) for i in str(curr))
    min_r = min(int(i) for i in str(curr))
    v3 = max_r == min_r

    if v1:
        s1 = 0
    else:
        s1 = f(curr + int(str(curr)[-1]), end)

    if v2:
        s2 = 0
    else:
        s2 = f(curr * int(str(curr)[0]), end)

    if v3:
        s3 = 0
    else:
        s3 = f(curr + (max_r - min_r), end)

    return s1 + s2 + s3

print(f(21, 62))