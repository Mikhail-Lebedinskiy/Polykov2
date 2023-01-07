def chetko(N):
    if N % 2 == 0:
        return True
    return False


for N in range(1,10000):
    N_bin = bin(N)
    N_str = str(N_bin)
    if chetko(N) == True:
        N_str = "10" + N_str[2:]
    elif chetko(N) == False:
        N_str = "1" + N_str[2:] + "01"
    a = int(N_str, 2)
    if a > 441:
        print(N)
        break