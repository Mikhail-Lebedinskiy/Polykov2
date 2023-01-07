for i in range(1000, 0, -1):
    N = i
    N -= N % 4
    N_bin = bin(N)[2:]
    N_bin += str(N_bin.count('1') % 2)
    N_bin += str(N_bin.count('1') % 2)
    R = int(N_bin, base=2)
    if R < 64:
        print(i)
        break