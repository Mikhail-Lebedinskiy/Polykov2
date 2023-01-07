def f(n):
    divisors = []
    for i in range(1003, 10 ** 4, 10):
        if n % i == 0:
            divisors.append(i)
    if len(divisors) == 3:
        return divisors
    return -1


counter = 0
for i in range(97 ** 3 + 1, 10 ** 9):
    if counter == 5:
        break
    divisors = f(i)
    if divisors == -1:
        continue
    print(i, min(divisors))
    counter += 1
