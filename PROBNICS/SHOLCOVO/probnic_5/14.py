def from_decimal_to_base(n, base):
    s = '0123456789ABCDEF'
    answer = ''
    while n != 0:
        answer += s[n % base]
        n //= base
    return answer[::-1]


n = 4 ** 700 + 4 ** 100 - 16 ** 100 - 64
print(from_decimal_to_base(n, 4).count('3'))