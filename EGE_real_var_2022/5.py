for i in range(1, 1000):
    N = i
    N_bin = bin(N)[2:]
    if N_bin.count('1') % 2 == 0:
        R_bin = '10' + N_bin[2:] + '0'
    else:
        R_bin = '11' + N_bin[2:] + '1'
    R = int(R_bin, 2)
    if R >= 16:
        print(i)
        break