def from_decimal_to_base(n: int, base: int) -> str:
    response = ''
    while n != 0:
        response += str(n % base)
        n //= base
    return response[::-1]


def from_base_to_decimal(n: str, base: int) -> int:
    response = 0
    for i, d in enumerate(n[::-1]):
        response += int(d) * base ** i
    return response


for i in range(1000, 1, -1):
    N = i
    N_6 = from_decimal_to_base(N, 6)
    N_6 += N_6[-1]
    N_2 = bin(from_base_to_decimal(N_6, 6))[2:]
    N_2 += N_2[-1]
    N = from_base_to_decimal(N_2, 2)
    if N < 344:
        print(i)
        break

