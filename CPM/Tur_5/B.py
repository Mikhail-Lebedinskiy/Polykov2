def bin_search(number_of_fogs, heights, delta):
    right, left = number_of_fogs - 1, 0
    while right - left > 1:
        mid = (right + left) // 2
        if heights[mid] + delta >= 0:
            right = mid
        else:
            left = mid
    if heights[right] + delta < 0:
        return right
    elif heights[left] + delta < 0:
        return left
    else:
        return -1
"""
[-13, -11, -10, -10, -5, 2, 3, 13, 14, 16]
[-27, -25, -24, -24, -19, -12, -11, -1, 0, 2]
"""

def f1(number_of_fogs, last_index, curr_index, heights, cur_delta, all_delta, positive_sum, negative_sum):
    negative_sum += (last_index + 1) * abs(cur_delta)
    s = 0
    # [0, 1, 2]
    # [-2, -1, 0]
    for index in range(last_index + 1, curr_index + 1):
        s += heights[index] + (all_delta - cur_delta)
    s = abs(s)
    negative_sum += abs(cur_delta) * (curr_index - last_index) - s
    positive_sum = positive_sum - s - abs(cur_delta) * (number_of_fogs - curr_index - 1)
    return positive_sum, negative_sum


def f2(number_of_fogs, last_index, curr_index, heights, cur_delta, all_delta, positive_sum, negative_sum):
    """
        last_index = 5
        curr_index = 2
    """
    s = 0
    for index in range(curr_index + 1, last_index + 1):
        s += heights[index] + (all_delta - cur_delta)
    s = abs(s)
    positive_sum += (number_of_fogs - last_index - 1) * abs(cur_delta)
    positive_sum += (last_index - curr_index) * abs(cur_delta) - s
    negative_sum = negative_sum - s - abs(cur_delta) * (curr_index + 1)
    return positive_sum, negative_sum


def main():
    number_of_fogs = int(input())
    heights = [int(i) for i in input().split()]
    heights.sort()

    number_of_days = int(input())
    deltaes = [int(i) for i in input().split()]

    current_delta = 0
    last_index_of_maximum_negative = bin_search(number_of_fogs, heights, 0)
    negative_sum = 0
    positive_sum = 0
    for height in heights:
        if height < 0:
            negative_sum += -height
        else:
            positive_sum += height
    # print(f'index = {last_index_of_maximum_negative}')
    # print(f'negative_sum = {negative_sum}')
    # print(f'positive_sum = {positive_sum}')

    for delta in deltaes:
        current_delta += delta
        current_index_of_maximum_negative = bin_search(number_of_fogs, heights, current_delta)
        # print(heights)
        # print(f'current_delta = {current_delta}')
        # print(f'index = {current_index_of_maximum_negative}')
        if current_index_of_maximum_negative >= last_index_of_maximum_negative and delta < 0:
            positive_sum, negative_sum = f1(number_of_fogs, last_index_of_maximum_negative,
                                            current_index_of_maximum_negative, heights, delta, current_delta,
                                            positive_sum, negative_sum)
        else:
            positive_sum, negative_sum = f2(number_of_fogs, last_index_of_maximum_negative,
                                            current_index_of_maximum_negative, heights, delta, current_delta,
                                            positive_sum, negative_sum)
        print(positive_sum + negative_sum)
        last_index_of_maximum_negative = current_index_of_maximum_negative



# print(bin_search(12, [-12, -10, -7, -4, -3, -1, 0, 1, 2, 3, 10, 11], 0))
# arr = [-12, -10, -7, -4, -3, -1, 0, 1, 2, 3, 10, 11]
# arr1 = [i - 3 for i in arr]
# arr2 = [i + 5 for i in arr]
# print(f1(12, 5, 8, arr, -3, -3, 27, 37))
# print(f2(12, 5, 2, arr, 5, 5, 27, 37))
# print(arr)
# print(arr2)
# print(arr1)

main()


