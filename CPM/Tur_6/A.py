def bin_search(arr, x, right):
    left = 0
    while right - left > 1:
        mid = (left + right) // 2
        if 10 * arr[mid] >= 9 * x:
            right = mid
        else:
            left = mid
    if 10 * arr[left] >= 9 * x:
        return left
    return right


number_of_files = int(input())

sizes = [int(i) for i in input().split()]
sizes.sort()


answer = 0
for i in range(number_of_files):
    x = bin_search(sizes, sizes[i], i)
    answer += i - x
print(answer)



# arr = [1, 2, 5, 7, 9, 15, 28.8, 29, 30, 32, 36]
#
# print(bin_search(arr, 32, 8))
# print(32 * 0.9)