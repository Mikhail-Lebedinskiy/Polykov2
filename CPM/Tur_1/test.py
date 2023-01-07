
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return low


arr = [1, 2, 10, 10, 10, 15, 16, 17]
x = 10

print(binary_search(arr, x))