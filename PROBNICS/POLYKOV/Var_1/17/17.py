def load_data(file_path):
    with open(file_path) as file:
        arr = [int(i) for i in file]
    return arr


def main():
    arr = load_data('data.txt')
    min_52, max_52 = 10 ** 5, -1
    for num in arr:
        if str(num)[-2:] == '52':
            min_52 = min(min_52, num)
            max_52 = max(max_52, num)
    r = max_52 - min_52
    answer = []
    for i in range(1, len(arr)):
        if min(arr[i - 1], arr[i]) < r < max(arr[i - 1], arr[i]):
            answer.append(arr[i - 1] + arr[i])
    print(len(answer), max(answer))


if __name__ == '__main__':
    main()