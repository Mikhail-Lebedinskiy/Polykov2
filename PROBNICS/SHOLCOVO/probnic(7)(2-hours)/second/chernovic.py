from itertools import product


arr = product(range(3))
arr = product(arr, range(2))
arr = product(arr, range(3))

p = [range(3), range(2), range(1)]
arr = product(*p)
print(*arr)