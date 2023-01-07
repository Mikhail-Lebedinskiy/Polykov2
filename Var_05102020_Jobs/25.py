for number in range(321655, 654322, 2):
    divisors = set()
    for divisor in range(2, int(number ** 0.5)):
        if number % divisor == 0:
            divisors.add(divisor)
            divisors.add(number // divisor)
    if len(divisors) > 70:
        print(f'{number}_{max(divisors)}', end='_')
