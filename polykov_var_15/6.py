for i in range(10000, 0, -1):
    s = i
    n = 121
    while s < 124:
        s = s + 10
        n = n + 17
    if n == 291:
        print(i)
        break