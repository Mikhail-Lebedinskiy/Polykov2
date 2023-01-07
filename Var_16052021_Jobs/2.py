from itertools import product, permutations


print('a b c d')
arr1 = []
for a, b, c, d in product([False, True], repeat=4):
    v1 = a and b
    v2 = not c
    p1 = v1 == v2
    p2 = b <= d
    if p1 and p2:
        arr1.append([int(i) for i in (a, b, c, d)])
        print(*[int(i) for i in (a, b, c, d)])
arr2 = [
    [1, 0, 0, 0],
    [1, 0, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 0]
]
for head in permutations([0, 1, 2, 3]):
    arr3 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for i in range(4):
        for l, j in enumerate(head):
            arr3[i][l] = arr2[i][j]
    for i in arr3:
        if i not in arr1:
            break
    else:
        print(arr3)
        print(head)


