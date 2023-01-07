def from_decimal_to_base(n: int, base: int) -> str:
    response = ''
    while n != 0:
        response += str(n % base)
        n //= base
    return response[::-1]


for x in range(1, 1000):
    n = 3*7**(x+1) + 13 * 7 ** (x+2) + 31 * 7 ** (3*x) + 7 ** (2 * x)
    n = from_decimal_to_base(n, 7)
    ans = 0
    for i in n:
        ans += int(i)
    if ans == 18:
        print(x)
        break
