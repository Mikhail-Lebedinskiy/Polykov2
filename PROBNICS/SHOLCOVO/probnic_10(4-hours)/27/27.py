def main():
    with open('27B.txt') as file:
        N = int(file.readline())
        numbers = [i.strip() for i in file]

    answer = []
    for i in range(N):
        for j in range(i + 1, N):
            if numbers[i] + numbers[j] == (numbers[i] + numbers[j])[::-1]:
                answer.append((int(numbers[i]), int(numbers[j])))
    print(answer)
    print(max([i[0] + i[1] for i in answer]))


main()