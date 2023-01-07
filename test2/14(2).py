def from_decimal_to_base(n, base):
    a = '0123456789ABCDEF'
    answer = ''
    while n != 0:
        answer += a[n % base]
        n //= base
    return answer[::-1]


n = 15 * 1728 ** 8 + 9 * 144 ** 12 + 7 * 12 ** 12 + 154
n_in_12 = from_decimal_to_base(n, 12)
print(n_in_12.count('0'))

