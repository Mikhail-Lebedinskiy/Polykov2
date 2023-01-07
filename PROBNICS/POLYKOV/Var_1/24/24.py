from math import prod


def load_data(file_path):
    with open(file_path) as file:
        s = file.readline().strip()
    return s


def is_good(num, mask):
    if not num.isdecimal():
        return False
    if len(num) != len(mask):
        return False
    for i in range(len(num)):
        if mask[i] == '?':
            continue
        if mask[i] != num[i]:
            return False
    return True


def solve(s):
    arr = s.split('KK')
    max_num = -1
    # arr = [i for i in arr if i.isdecimal()]
    # arr = [i for i in arr if len(i) == len('43??78???')]
    for segment in arr:
        if is_good(segment, '43??78???34'):
            max_num = max(max_num, int(segment))
    print(max_num)
    return prod([int(i) for i in str(max_num) if int(i) % 2 == 1])


def main():
    s = load_data('data.txt')
    print(solve(s))


if __name__ == '__main__':
    main()


# print(is_good('430178010', '43??78???'))
# print(is_good('430A78010', '43??78???'))
# print(is_good('43017801', '43??78???'))
