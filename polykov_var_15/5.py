good_R = []
for i in range(1, 10000):
    N = i
    N_bin = bin(N)[2:]
    if N % 2 == 0:
        N_bin += '01'
    else:
        N_bin += '10'
    R = int(N_bin, 2)
    if R > 81:
        good_R.append(R)
print(min(good_R))