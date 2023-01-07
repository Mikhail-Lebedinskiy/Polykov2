from itertools import product


def from_decimal_to_base(n: int, base: int) -> str:
    response = ''
    while n != 0:
        response += str(n % base)
        n //= base
    return response[::-1]


def from_base_to_decimal(number: str, base: int) -> int:
    number = number[::-1]
    response = 0
    for i in range(len(number)):
        response += int(number[i]) * base ** i
    return response


def is_good_number(number: str) -> bool:
    if '3' not in number:
        return False
    number = from_decimal_to_base(from_base_to_decimal(number, 9) * 3, 9)
    if len(number) == 3:
        return True
    return False


good_numbers = []
for number in [''.join(i) for i in product('012345678', repeat=3)]:
    if number[0] == '0':
        continue
    if is_good_number(number):
        good_numbers.append(from_base_to_decimal(number, 9))
print(from_decimal_to_base(min(good_numbers) + max(good_numbers), 9))
