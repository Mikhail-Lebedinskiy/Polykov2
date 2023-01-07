def load_data(file_path):
    arr = []
    with open(file_path) as file:
        n = int(file.readline())
        for line in file:
            arr.append([int(i) for i in line.split()])
    return n, arr


def solve(n, arr):
    counter = {}
    for x, y in arr:
        try:
            counter[y].append(x)
        except KeyError:
            counter[y] = [x]
    max_count, max_y = -1, -1
    for y in counter:
        if len(counter[y]) == max_count:
            max_y = max(max_y, y)
        elif len(counter[y]) > max_count:
            max_count = len(counter[y])
            max_y = y
    print(max_y, counter[max_y])
    arr = [int(str(i)[:-1]) for i in counter[max_y]]
    print(arr)
    print('ANSWER')
    print(max_y)
    print(len(set([i for i in arr if -90 < i < 90])))



def main():
    n, arr = load_data('data.txt')
    solve(n, arr)


if __name__ == '__main__':
    main()