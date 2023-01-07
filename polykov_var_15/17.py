def from_decimal_to_base(n, base):
    answer = ''
    numbers = '0123456789'
    while n > 0:
        answer += numbers[n % base]
        n //= base
    return answer[::-1]


f = open('17-7.txt', 'r')
arr = [int(i) for i in f]
f.close()

answer = []
for num in arr:
    num_8 = from_decimal_to_base(num, 8)
    if num_8[-1] == '7' and num_8[-2:] != '27':
        answer.append(num)

print(len(answer), max(answer))
