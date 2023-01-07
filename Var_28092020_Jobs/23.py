def f(n, end):
    if n == end:
        return 1
    if n > end:
        return 0
    if (n % 100) // 10 == 9:
        return f(n + 1, end)
    return f(n + 1, end) + f(n + 10, end)


print(f(10, 33))
