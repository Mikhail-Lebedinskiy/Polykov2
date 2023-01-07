def get_divisors(n):
    if n % 2 == 0:
        return False
    response = []
    for i in range(1, int(n ** 0.5)):
        if n % i == 0:
            if n != i * i:
                response.append(i)
                response.append(n // i)
            else:
                response.append(i)
    return response


j = 0
for i in range(800001, 800001 * 10**5, 2):
    print(i)
    divisors = get_divisors(i)
    if len(divisors) > 10 and sum(divisors) % 2 == 1:
        print(i, len(divisors))
        j += 1
    if j == 6:
        break
