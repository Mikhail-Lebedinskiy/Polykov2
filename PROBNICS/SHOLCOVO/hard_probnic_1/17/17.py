def from_decimal_to_base(n, base):
    digits = '0123456789ABCDEF'
    answer = ''
    while n != 0:
        answer += digits[n % base]
        n //= base
    return answer[::-1]


numbers = [int(i) for i in open('17__wi30.txt')]
print(numbers[1: 10])
max_number = max([i for i in numbers if i % 127 == 0])

answers = []
for i in range(1, len(numbers)):
    x1, x2 = numbers[i - 1], numbers[i]
    if x1 > max_number or x2 > max_number:
        if '31' in from_decimal_to_base(x1, 8) or '31' in from_decimal_to_base(x2, 8):
            answers.append(x1 + x2)

print(len(answers))
print(min(answers))