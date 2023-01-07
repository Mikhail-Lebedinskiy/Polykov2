def f(cur, end):
    if cur == end:
        return 1
    if cur > end:
        return 0
    return f(cur + 1, end) + f(cur + 3, end)


print(f(5, 15) * f(15, 25) - f(5, 12) * f(12, 15))

