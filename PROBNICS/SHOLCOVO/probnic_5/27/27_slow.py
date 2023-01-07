def load_data(file_name):
    with open(file_name) as file:
        pare_count = int(file.readline())
        pares = []
        for i in range(pare_count):
            pares.append([int(i) for i in file.readline().split()])
    return pare_count, pares


def main():
    pare_count, pares = load_data('27B__x9ch.txt')
    min_delta = 10 ** 9
    max_sum = 0
    for pare in pares:
        max_sum += max(pare)
        if pare[0] - pare[1] % 35 != 0:
            min_delta = min(min_delta, abs(pare[0] - pare[1]))
    if max_sum % 35 != 0:
        return max_sum
    else:
        return max_sum - min_delta


print(main())

