answer = []
for i in range(10 ** 4):
    N = i
    N_bin = bin(N)[2:]
    N_bin = N_bin[1:]
    if N_bin.count('1') % 2 == 0:
        N_bin = '10' + N_bin
    else:
        N_bin = '1' + N_bin + '0'
    R = int(N_bin, 2)
    if R < 450:
        answer.append(R)
print(max(answer))