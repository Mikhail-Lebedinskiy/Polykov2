for i in range(1, 10 ** 4):
    N = i
    N_bin = bin(N)[2:]

    N_bin += str(N_bin.count('1') % 2)
    N_bin += str(N_bin.count('1') % 2)
    R = int(N_bin, 2)
    if R > 500:
        print(N)
        break