def from_decimal_to_base(n, base):
    s = '0123456789ABCDEF'
    d = {i: s[i] for i in range(16)}
    answer = ''
    while n != 0:
        answer += d[n % base]
        n //= base
    return answer[::-1]


def from_base_to_decimal(n, base):
    s = '0123456789ABCDEF'
    d = {s[i]: i for i in range(16)}
    answer = 0
    n = n[::-1]
    for i, deg in enumerate(n):
        answer += d[deg] * base ** i
    return answer

for x in '0123456789ABCDEF':
    v1 = from_base_to_decimal(f'2{x}BAD', 16)
    v2 = from_base_to_decimal(f'3C{x}FE', 16)
    if (v1 + v2) % 15 == 0:
        print(x)
        print((v1 + v2) / 15)

# print(from_base_to_base('10', 16))
# print(from_base_to_base('19', 16))
# print(from_base_to_base('F', 16))

# print(from_base_to_decimal('25BAD', 16))
# print(13 + 10 * 16 + 11 * 16 ** 2 + 5 * 16 ** 3 + 2 * 16 ** 4)