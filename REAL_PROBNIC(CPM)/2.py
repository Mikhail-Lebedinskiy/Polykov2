from itertools import product, permutations

def f(arr, ind):
    r = []
    for i in ind:
        r.append(arr[i])
    r.append(arr[4])
    return r


print('x y z w F')
data = []
for x, y, z, w in product([0, 1], repeat=4):
    v1 = y == z
    v2 = w <= v1
    z1 = z <= x
    z2 = y == z1
    V = v2 and z2
    data.append([x, y, z, w, int(V)])
    print(x, y, z, w, int(V))

print(data)
# print('*' * 100)
p = [[[0, 0, 0, 0, 1], [1, 0, 0, 0, 1]], [[0, 0, 1, 1, 1], [0, 1, 1, 1, 1]], [[0, 0, 0, 1, 0]]]
for answer in permutations('xyzw'):
    t = []
    for chr in answer:
        d = {'x' : 0, 'y': 1, 'z': 2, 'w': 3}
        t.append(d[chr])
    flag = True
    for k in p:
        for x in k:
            # print(f(x, t))
            if f(x, t) in data:
                break
        else:
            flag = False
            break
    if flag:
        print(*answer)

