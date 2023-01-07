def load_data(file_path: str) -> list:
    response = []
    with open(file_path) as file:
        file.readline()
        for line in file:
            response.append(int(line.strip()))
    return response


def main() -> int:
    arr = [[0, 0]]
    i = 0
    for number in load_data('data/Задание 27/27-B.txt'):
        if number == 0:
            arr.append([0, 0])
            i += 1
        else:
            arr[i][number % 2] += 1

    chet_num = arr[0][0]
    not_chet_num = arr[0][1]
    answer = 0
    for i in arr[1:]:
        answer += i[0] * chet_num
        answer += i[1] * not_chet_num
        chet_num += i[0]
        not_chet_num += i[1]
    return answer


if __name__ == '__main__':
    print(main())
