def f(n):
    if '5' in str(n):
        return 0
    if n == 60:
        return 1
    if n > 60:
        return 0
    return f(n + 1) + f(n * 2)

print(f(1))

