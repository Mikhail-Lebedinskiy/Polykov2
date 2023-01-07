from math import prod


def is_good_line(line):
    all_prod = prod(line)
    all_sum = sum(line)
    flag = True
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if 2 * (line[i] + line[j]) == all_sum:
                flag = False
    if flag:
        return False
    if (min(line) * max(line)) ** 2 == all_prod:
        return True
    return False


def main():
    table = []
    with open('9.txt') as file:
        for line in file:
            table.append([int(i) for i in line.split()])

    answer = 0
    for line in table:
        if is_good_line(line):
            print(line)
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()