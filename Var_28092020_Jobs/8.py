from itertools import product


arr = [''.join(i) for i in product('АЛГОРИТМ', repeat=4)]
arr.sort()
answer = -1
# print(arr)
for i in range(len(arr)):
    if arr[i][-2:] == 'ИМ':
        answer = i + 1
print(answer)