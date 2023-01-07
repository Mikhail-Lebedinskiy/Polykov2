def d(n):
    divisors = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    return divisors


def search_prime_divisors(n):
    prime_divisors = []
    d = 2
    while n != 1:
        if n % d == 0:
            prime_divisors.append(d)
            n //= d
        else:
            d += 1
    return prime_divisors


print(search_prime_divisors(500 * 10**6 + 3))