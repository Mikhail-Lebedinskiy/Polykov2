def from_decimal_to_base(n, base):
    s = '0123456789'
    answer = ''
    while n != 0:
        answer += s[n % base]
        n //= base
    return answer[::-1]


n = 559
for base in range(2, 11):
    sum_of_digits = sum([int(i) for i in from_decimal_to_base(n, base)])
    if sum_of_digits % 2 == 1:
        print(base)