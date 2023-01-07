def from_decimal_to_base(n, base):
    digits = '0123456789ABCDEF'
    answer = ''
    while n != 0:
        answer += digits[n % base]
        n //= base
    return answer[::-1]


print(from_decimal_to_base(1365, 2))
print(from_decimal_to_base(682, 2))
print(from_decimal_to_base(2**64, 2))
print(len(from_decimal_to_base(2**64, 2)))
print(2 ** (65 - 11))
