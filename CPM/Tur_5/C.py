def f(n, prime_numbers):
    response = []
    for prime_number in prime_numbers:
        n_ = n
        deg = 0
        while True:
            if n_ % prime_number == 0:
                deg += 1
                n_ //= prime_number
            else:
                break
        if deg % 2 == 1:
            response.append(prime_number)
    return tuple(response)



n = int(input())
factorize = [[] for i in range(n + 1)]

for i in range(2, n + 1):
    if not factorize[i]:
        for j in range(i, n + 1, i):
            factorize[j].append(i)

data = {}

for i in range(1, n + 1):
    if not factorize[i]:
        try:
            data[()] += 1
        except KeyError:
            data[()] = 1
    else:
        resp = f(i, factorize[i])
        try:
            data[resp] += 1
        except KeyError:
            data[resp] = 1

answer = 0
for value in data.values():
    if value >= 3:
        answer += value * (value - 1) * (value - 2) // 6


print(answer)

