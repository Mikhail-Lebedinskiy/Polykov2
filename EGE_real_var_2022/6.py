for i in range(-100, 100):
    s = (i - 21) // 10
    n = 1
    while s >= 0:
        n = n * 2
        s = s - n
    if n == 8:
        print(i)
        break
