def from_decimal_to_base(n, base):
    answer = ''
    while n > 0:
        answer += str(n % base)
        n //= base
    return answer[::-1]


n = 7 ** 2103 - 6 * 7 ** 1270 + 3 * 7 ** 57- 98
n_7 = from_decimal_to_base(n, 7)
answer = 0
for digit in n_7:
    answer += int(digit)
print(answer)
