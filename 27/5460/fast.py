class CircularList():
    def __init__(self, data=None):
        if data is None:
            self.data = []
            self.len = 0
            self.sum = 0
        else:
            self.data = data.copy()
            self.len = len(data)
            self.sum = sum(data)

    def __iadd__(self, other):
        self.data.append(other)
        self.len += 1
        self.sum += other
        return self

    def __len__(self):
        return self.len

    def __getitem__(self, key):
        return self.data[key % self.len]

    def __str__(self):
        return str(self.data)

    def sum(self):
        return self.sum()


def load_data(file_path):
    with open(file_path) as file:
        points = CircularList()
        count_of_points = int(file.readline())
        for i in range(count_of_points):
            points += int(file.readline())
    return count_of_points, points


def sum_of_sigment(start_point, len_of_sigment, partial_sums, len_of_partial_sums):
    if start_point + len_of_sigment < len_of_partial_sums:
        if start_point != 0:
            return partial_sums[start_point + len_of_sigment] - partial_sums[start_point - 1]
        return partial_sums[start_point + len_of_sigment]
    return partial_sums[-1] - partial_sums[start_point - 1] + \
           partial_sums[start_point + len_of_sigment - len_of_partial_sums]


def f(start_point, points, count_of_points, all_rubbish, partial_sums, len_of_partial_sums):
    left, right = 0, len_of_partial_sums - 1
    while True:
        mid = (left + right) // 2
        # print('#', left, right, mid)
        if left == mid:
            return mid
        if sum_of_sigment(start_point, mid, partial_sums, len_of_partial_sums) > all_rubbish / 2:
            right = mid
        else:
            left = mid


def main(file_path):
    count_of_points, points = load_data(file_path)
    all_rubbish = points.sum
    partial_sums = []
    for i in range(count_of_points):
        try:
            partial_sums.append(partial_sums[i-1] + points[i])
        except IndexError:
            partial_sums.append(points[i])
    len_of_partial_sums = len(partial_sums)

    min_sum = 10 ** 9
    min_len = 10 ** 9
    for i in range(count_of_points):
        x = f(i, points, count_of_points, all_rubbish, partial_sums, len_of_partial_sums)
        cur_sum = sum_of_sigment(i, x, partial_sums, len_of_partial_sums)
        if max(cur_sum, all_rubbish - cur_sum) < min_sum:
            min_sum = max(cur_sum, all_rubbish - cur_sum)
            min_len = x
        elif max(cur_sum, all_rubbish - cur_sum) == min_sum:
            min_len = min(min_len, x)
        cur_sum = sum_of_sigment(i, x + 1, partial_sums, len_of_partial_sums)
        if max(cur_sum, all_rubbish - cur_sum) < min_sum:
            min_sum = max(cur_sum, all_rubbish - cur_sum)
            min_len = x + 1
        elif max(cur_sum, all_rubbish - cur_sum) == min_sum:
            min_len = min(min_len, x)
    print('answer')
    print(min_len, min_sum)


    # print(count_of_points)
    # print(points)
    # print(all_rubbish)
    # print(partial_sums)
    # print(sum_of_sigment(1, 5, partial_sums, len_of_partial_sums))
    # x = f(2, points, count_of_points, all_rubbish, partial_sums, len_of_partial_sums)
    # print(x)
    # print(sum_of_sigment(2, x, partial_sums, len_of_partial_sums))


main('data/test.txt')
main('data/A.txt')
main('data/B.txt')
