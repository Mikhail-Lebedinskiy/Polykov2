for i in range(1, 10000000):
    x = i
    a, b = 0, 1
    while x > 0:
        if (x % 2) > 0:
            a += 1
        else:
            b += x % 5
        x = x // 5
    if a == 2 and b == 9:
        print(i)
        break


