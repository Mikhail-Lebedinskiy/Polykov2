for i in range(1, 1000):
    N = i
    N_bin = bin(N)[2:]
    if N % 2 == 0:
        N_bin = '10' + N_bin
    else:
        N_bin = '1' + N_bin + '01'
    R = int(N_bin, 2)
    if R > 441:
        print(N)
        break
