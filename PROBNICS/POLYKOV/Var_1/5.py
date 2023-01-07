answer = 0
for i in range(1000, 10000):
    N = i
    N_str = str(N)
    R = N_str
    if int(N_str[0]) % 4 == 0:
        R = '9' + N_str[1:]
    elif int(N_str[0]) % 2 == 0:
        R = '3' + N_str[1:]
    if R[0] == '9' and int(R) % 8 == 4:
        answer += 1


print(answer)