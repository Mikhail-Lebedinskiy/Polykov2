def from_decimal_to_base(n, base):
    answer = ''
    while n != 0:
        answer += str(n % base)
        n //= base
    return answer[::-1]


n = 7 * 512 ** 1912 + 6 * 64 ** 1994 - 5 * 8 ** 1991 - 4 * 8 ** 1960 - 2022

n_in_8 = from_decimal_to_base(n, 8)

print(n_in_8.count('7'))
