def f(number: list):
    answer = 0
    for i, digit in enumerate(number[::-1]):
        answer += digit * 158 ** i
    return answer

def main():
    answer = 0
    for x in range(158):
        num1 = [2, 7, 3, x, 2]
        num2 = [1, x, 3, 9, 0]
        res = f(num1) + f(num2)
        if res % 73 == 0:
            answer += res // 73
    return answer


print(main())
