for i in range(1, 10000):
    s = i
    s = (s - 10) // 7
    n = 1
    while s > 0:
        n = n * 2
        s = s - n
    if n == 8:
        print(i)
        break