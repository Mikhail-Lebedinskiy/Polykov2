from itertools import product


def math_expression(*arg):
    """ЗАПИШИТЕ СЮДА ВАШЕ МАТЕМАТИЧОСКОЕ ВЫРАЖЕНИЕ"""
    return (19 * arg[0] + arg[1]) ** 18 + (arg[0] + arg[1]) ** 18 + (arg[0] + 19 * arg[1]) ** 18 - arg[2] ** 2


prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]


moduls = []
max_deg = 4
get_prime_numbers = {}

for p in prime_numbers:
    for deg in range(1, max_deg):
        get_prime_numbers[p ** deg] = p
        moduls.append(p ** deg)

count_of_args = 3  # введите количество переменых

for module in moduls:
    for args in product(range(module), repeat=count_of_args):
        if math_expression(*args) % module == 0:
            break
    else:
        print(module)

