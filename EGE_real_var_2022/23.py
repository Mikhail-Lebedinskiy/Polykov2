def f(curr, end):
    if curr == end:
        return 1
    if curr < end:
        return 0
    return f(curr - 1, end) + f(curr // 2, end)


print(f(30, 12) * f(12, 1))