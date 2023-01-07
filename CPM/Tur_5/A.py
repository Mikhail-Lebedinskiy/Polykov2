def f(a, b):
    x1, x2 = a, b
    deg_2 = 0
    while True:
        if x1 % 2 == 0:
            x1 //= 2
            deg_2 += 1
        else:
            break
    return (x1 + a * b // x1) * 2


a, b = [int(i) for i in input().split()]

print(max(f(a, b), f(b, a)))
