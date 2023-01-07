def load_data(file_path: str) -> list[list]:
    response = []
    with open(file_path) as file:
        for line in file:
            response.append([int(i) for i in line.strip().split(';')])
    return response


def go(data: list) -> tuple[int, list]:
    arr = [[0] * len(data[0]) for i in range(len(data))]
    print(*data)

    arr[0][0] = data[0][0]
    for i in range(1, len(data[0])):
        # заполняем верхнюю строку
        arr[0][i] = arr[0][i - 1] + data[0][i]

    for i in range(1, len(data)):
        # заполняем левый столбец
        arr[i][0] = arr[i - 1][0] + data[i][0]

    for row in range(1, len(data)):
        for column in range(1, len(data[row])):
            arr[row][column] = max(arr[row - 1][column], arr[row][column - 1]) + data[row][column]
    print(*arr)

    curr_row, curr_column = len(arr) - 1, len(arr[0]) - 1
    path_cords = []
    while True:
        data[curr_row][curr_column] = 0
        path_cords.append((curr_row, curr_column))
        if curr_row == 0 and curr_column == 0:
            break
        elif curr_row == 0:
            curr_row, curr_column = curr_row, curr_column - 1
        elif curr_column == 0:
            curr_row, curr_column = curr_row - 1, curr_column
        else:
            if arr[curr_row - 1][curr_column] > arr[curr_row][curr_column - 1]:
                curr_row, curr_column = curr_row - 1, curr_column
            else:
                curr_row, curr_column = curr_row, curr_column - 1
    return arr[len(arr) - 1][len(arr[0]) - 1], data.copy()


def main() -> tuple[int, int]:
    data = load_data('data/Задание 18/18.txt')
    x, data = go(data.copy())
    print('*' * 50)
    y, data = go(data.copy())
    return x, y


if __name__ == '__main__':
    print(main())