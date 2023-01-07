from itertools import permutations


for i in permutations([1, 2, 3, 4]):
    for j in i:
        print(j)