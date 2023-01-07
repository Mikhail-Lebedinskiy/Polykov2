n = 4 * 625 ** 1920 + 4 * 125 ** 1930 - 4 * 25 ** 1940 - 3 + 5 ** 1950 - 1960

answer = 0
while n != 0:
    if n % 5 == 0:
        answer += 1
    n //= 5
print(answer)
