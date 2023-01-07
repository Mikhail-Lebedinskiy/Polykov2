def f(N):
    N_str = str(N)
    minn = 100
    maxx = 0
    for i in range(len(N_str) - 1):
        if minn > int(N_str[i] + N_str[i+1]):
            minn = int(N_str[i] + N_str[i+1])
        if maxx < int(N_str[i] + N_str[i+1]):
            maxx = int(N_str[i] + N_str[i+1])
    return maxx - minn



for N in range(10, 100000):
    gg = f(N)
    if gg == 44:
        print(N)
        break



