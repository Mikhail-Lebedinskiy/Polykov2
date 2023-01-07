for i in range(10 ** 3, 0, -1):
    x = i
    K = 9 * x - 57
    D = 9 * x + 13
    while K * D > 0:
        if K > D:
            K = K % D
        else:
            D = D % K
    if K + D == 70:
        print(i)
        break