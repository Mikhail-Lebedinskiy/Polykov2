A = set()
P = set(range(1, 7))
Q = {3, 5, 15}

for x in range(1, 100000):
    v1 = x not in P
    v2 = x in Q
    v3 = x not in Q
    if not((v1 and v2) or v3):
        A.add(x)
print(len(A))