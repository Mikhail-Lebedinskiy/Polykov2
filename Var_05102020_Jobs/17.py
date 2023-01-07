def from_decimal_to_base(n: int, base: int) -> str:
    response = ''
    while n != 0:
        response += str(n % base)
        n //= base
    return response[::-1]


def is_good_number(n: int) -> bool:
    n_3 = from_decimal_to_base(n, 3)
    n_7 = from_decimal_to_base(n, 7)
    n_9 = from_decimal_to_base(n, 9)
    if n_3[-1] != '2' or n_7[-1] != '6' or n_9[-1] != '8':
        return False
    if n_3[1] == n_3[-1] or n_7[1] == n_7[-1] or n_9[1] == n_9[-1]:
        return False
    return True


good_numbers = []
for n in range(12345, 54322):
    n_2 = from_decimal_to_base(n , 2)
    n_6 = from_decimal_to_base(n, 6)
    n_8 = from_decimal_to_base(n, 8)
    if is_good_number(n):
        good_numbers.append(n)


print(max(good_numbers))
print(len(good_numbers))
