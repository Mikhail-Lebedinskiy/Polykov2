def from_decimal_to_base(n, base):
    digits = '0123456789ABCDEF'
    answer = ''
    while n != 0:
        answer += digits[n % base]
        n //= base
    return answer[::-1]


def from_base_to_decimal(n, base):
    answer = 0
    digits = '0123456789ABCDEF'
    d = {digits[i]: i for i in range(len(digits))}
    for i, digit in enumerate(n[::-1]):
        answer += d[digit] * base ** i
    return answer


for i in range(10 ** 6, 0, -1):
    N = i
    N_16 = from_decimal_to_base(N // 2, 16)
    if N % 4 != 0:
        N_16 = 'F' + N_16 + 'A0'
    else:
        N_16 = '15' + N_16 + 'C'
    R = from_base_to_decimal(N_16, 16)
    if R < 1048576:
        print(i)
        break

