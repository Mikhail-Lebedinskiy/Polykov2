for i in range(10, 10**7):
    N = str(i)
    arr = [int(N[j] + N[j + 1]) for j in range(len(N) - 1)]
    answer = max(arr) - min(arr)
    if N == '2022':
        print(answer)
"""159"""