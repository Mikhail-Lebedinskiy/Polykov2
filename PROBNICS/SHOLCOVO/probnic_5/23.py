def f(cur, end):
    if cur == end:
        return 1
    if cur < end:
        return 0
    return f(cur - 1, end) + f(cur // 3, end)


print(f(33, 9) * f(9, 1))
