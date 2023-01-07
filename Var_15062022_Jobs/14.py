def from_decimal_to_9(n):
    answer = ''
    while n != 0:
        answer += str(n % 9)
        n //= 9
    return answer[::-1]


x = 7 * 729 ** 543 - 6 * 81 ** 765 - 5 * 9 ** 987 - 20
x_9 = from_decimal_to_9(x)

print(x_9.count('8'))