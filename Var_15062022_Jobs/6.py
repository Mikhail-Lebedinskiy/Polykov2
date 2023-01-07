for i in range(-1000, 100):
    s = i
    s = (s + 13) * 10
    n = 515
    j = 0
    while s < 0 and j < 200:
        n = n // 2
        j += 1
        s = s + n
    if n == 8:
        print(i)
