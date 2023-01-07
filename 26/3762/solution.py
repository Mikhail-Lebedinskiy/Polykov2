def load_data(file_path: str) -> tuple[int, list]:
    numbers = []
    with open(file_path) as file:
        count = int(file.readline())
        for line in file:
            numbers.append(int(line))
    return count, numbers


def main() -> tuple[int, int]:
    count_of_numbers, numbers = load_data('data.txt')
    numbers_set = set(numbers)
    min_sum = 10**9
    count = 0
    for i in range(count_of_numbers):
        for j in range(i + 1, count_of_numbers):
            for l in range(j + 1, count_of_numbers):
                sum_of_three_numbers = numbers[i] + numbers[j] + numbers[l]
                if (sum_of_three_numbers % 3 == 0) and (sum_of_three_numbers // 3 in numbers_set):
                    count += 1
                    min_sum = min(min_sum, sum_of_three_numbers)
    return count, min_sum // 3


if __name__ == '__main__':
    print(main())