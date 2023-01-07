from random import randint


def generator(max_n=1000):
    n = randint(20, max_n)
    arr = [randint(1, 10 ** 4) for i in range(n)]
    return n, arr


def load_data(file_path):
    with open(file_path) as file:
        n = int(file.readline())
        arr = []
        for line in file:
            _, x = [int(i) for i in line.split()]
            arr.append(x)
    return n, arr


def slow_solution(n, arr):
    answer = -1
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] >= arr[j]:
                continue
            for k in range(i + 1, j):
                if arr[i] < arr[k]:
                    break
            else:
                answer = max(answer, j - i)
    return answer


def medium_solution(n, arr):
    answer = -1
    for i in range(n):
        segment_len = 0
        for j in range(i + 1, n):
            if arr[i] >= arr[j]:
                segment_len += 1
            else:
                break
        else:
            continue
        answer = max(answer, segment_len)
    return answer + 1


def test(count=100):
    for i in range(count):
        n, arr = generator()
        slow_answer = slow_solution(n, arr)
        medium_answer = medium_solution(n, arr)
        if slow_answer != medium_answer:
            print(slow_answer, medium_answer)
            print(n, arr)
        else:
            print('OK', slow_answer)


def main():
    # n, arr = load_data('test.txt')
    # print(slow_solution(n, arr))
    # print(medium_solution(n, arr))
    # test()
    n, arr = load_data('A.txt')
    answer_A = medium_solution(n, arr)
    n, arr = load_data('B.txt')
    answer_B = medium_solution(n, arr)
    print(answer_A, answer_B)



if __name__ == '__main__':
    main()