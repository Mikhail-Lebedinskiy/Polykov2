def resheto(start: int, end: int) -> list:
    response = []
    arr = [1] * (end + 1)
    for i in range(2, end + 1):
        if arr[i] == 1 and i >= start:
            response.append(i)
        for j in range(i, end + 1, i):
            arr[j] += 1
    return response


def main() -> None:
    prime_numbers = resheto(3, 1_000_000)
    for i in range(1, len(prime_numbers)):
        number1, number2 = prime_numbers[i - 1], prime_numbers[i]
        if number2 - number1 > 90:
            print(number1, number2)


main()
