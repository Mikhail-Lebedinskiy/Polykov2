for N in range(1000, 0, -1):
    bN = bin(N)[2:]
    if N % 2 == 0:
        bN += '10'
    else:
        bN += '01'
    R = int(bN, 2)
    if R < 171:
        print(N)
        break
