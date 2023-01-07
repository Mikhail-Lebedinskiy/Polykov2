from itertools import product


def get_number(request, substitution):
    answer = ''
    i = 0
    for chr in request:
        if chr == '?':
            answer += substitution[i]
            i += 1
        else:
            answer += chr
    return int(answer)


def binary_search(arr, x):
    def f(arr, i, n):
        while True:
            if arr[i] != n:
                return i + 1
            if i == 0:
                return i
            i -= 1
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return f(arr, mid, x)
    return low


def main():
    count_of_numbers, count_of_requests = [int(i) for i in input().split()]
    arr = dict()
    numbers = sorted([int(i) for i in input().split()])

    for _ in range(count_of_requests):
        request = input()
        sum = 0
        for substitution in product(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'], repeat=request.count('?')):
            number = get_number(request, substitution)
            try:
                sum += arr[number]
            except KeyError:
                arr[number] = count_of_numbers - binary_search(numbers, number)
                sum += arr[number]
        print(sum)

main()
