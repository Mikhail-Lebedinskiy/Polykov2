def is_good(num: str):
    ind_1 = num.find('1')
    ind_2 = num.rfind('68')
    if (ind_2 - ind_1) <= 2:
        return False
    if int(num) % 161 == 0:
        return True
    return False


def solve():
    answer = []
    for i in range(1, 17 * 10 ** 6 + 1):
        if is_good(str(i)):
            answer.append(i)
    print(*answer[::500])
    print(*[i // 161 for i in answer[::500]])


def main():
    solve()


if __name__ == '__main__':
    main()
