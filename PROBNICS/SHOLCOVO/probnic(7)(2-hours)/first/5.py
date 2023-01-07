# def f(i):
#     N = i
#     N_bin = bin(N)[2:]
#     if N % 2 == 0:
#         N_bin = '10' + N_bin + '1'
#     else:
#         N_bin = '1' + N_bin + '01'
#     R = int(N_bin, 2)
#     return R


for i in range(1, 10 ** 4):
    N = i
    N_bin = bin(N)[2:]
    if N % 2 == 0:
        N_bin = '10' + N_bin + '1'
    else:
        N_bin = '1' + N_bin + '01'
    R = int(N_bin, 2)
    if R > 420:
        print(N)
        break

