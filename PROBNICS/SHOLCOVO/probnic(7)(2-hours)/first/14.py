def from_decimal_to_base(n, base):
    answer = ''
    while n != 0:
        answer += str(n % base)
        n //= base
    return answer[::-1]


n = 7 ** 103 + 6 * 7 ** 104 - 3 * 7 ** 57 + 98

answer = 0
for deg in from_decimal_to_base(n, 7):
    answer += int(deg)

print(answer)