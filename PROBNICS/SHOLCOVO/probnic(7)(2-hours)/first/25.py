def f(arr):
    for i in range(1, len(arr) - 1):
        if arr[i] - arr[i - 1] != arr[i + 1] - arr[i]:
            return False
    return True


resheto = [[] for i in range(5 * 10 ** 5 + 1)]
for i in range(2, 5 * 10 ** 5 + 1):
    if not resheto[i]:
        for j in range(i, 5 * 10 ** 5 + 1, i):
            resheto[j].append(i)



for i in range(10 ** 5, 5 * 10 ** 5 + 1):
    if len(resheto[i]) > 3 and f(resheto[i]):
        print(i, len(resheto) * (resheto[i][1] - resheto[i][0]))

print(resheto[101065])

print(f([i for i in range(11, 1000, 15)]))
print(f([1, 2, 3, 45, 45, 45]))
