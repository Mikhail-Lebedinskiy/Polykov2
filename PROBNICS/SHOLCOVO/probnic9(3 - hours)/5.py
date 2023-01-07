# def f(N):
#     N_bin = bin(N)[2:]
#     N_bin += N_bin[-2]
#     N_bin += N_bin[1]
#     R = int(N_bin, 2)
#     return R


answer = 0
for i in range(2, 10 ** 3):
    N = i
    N_bin = bin(N)[2:]
    N_bin += N_bin[-2]
    N_bin += N_bin[1]
    R = int(N_bin, 2)
    if 100 <= R <= 150:
        answer += 1
print(answer)
