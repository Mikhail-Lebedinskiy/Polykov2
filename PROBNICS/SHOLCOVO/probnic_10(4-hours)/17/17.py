def main():
    with open('17.txt') as file:
        numbers = [int(i) for i in file]
    max_131 = max([i for i in numbers if i % 131 == 0])
    answer = []
    for i in range(1, len(numbers)):
        if max(numbers[i], numbers[i - 1]) <= max_131:
            continue
        if '11' in str(numbers[i]) or '11' in str(numbers[i - 1]):
            answer.append(numbers[i] + numbers[i - 1])
    print(max_131)
    print(len(answer))
    print(min(answer))


if __name__ == '__main__':
    main()