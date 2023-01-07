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


for N in range(10, 100):
    N_16 = from_decimal_to_base(N, 16)
    N_9 = from_decimal_to_base(N, 9)
    if N_16[-1] == 'C' and N_9[-1] == '4':
        print(N)