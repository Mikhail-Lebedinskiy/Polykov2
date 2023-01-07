from random import randint


def slow_main(number_of_fogs, heights, number_of_days, deltaes):
    answers = []
    for delta in deltaes:
        for i in range(number_of_fogs):
            heights[i] += delta
        positive_sum = 0
        negative_sum = 0

        for height in heights:
            if height < 0:
                negative_sum += -height
            else:
                positive_sum += height
        answers.append((positive_sum, negative_sum))
    return answers.copy()


def fast_main(number_of_fogs, heights, number_of_days, deltaes):
    answers = []

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


    heights.sort()
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
        answers.append((positive_sum, negative_sum))
        last_index_of_maximum_negative = current_index_of_maximum_negative
    return answers.copy()


def data_generate():
    number_of_fogs = 10
    heights = [randint(-20, 20) for i in range(number_of_fogs)]
    number_of_days = 5
    deltaes = [randint(-15, 15) for i in range(number_of_days)]
    return number_of_fogs, heights, number_of_days, deltaes


def test():
    for _ in range(1000):
        number_of_fogs, heights, number_of_days, deltaes = data_generate()
        answer1 = fast_main(number_of_fogs, heights.copy(), number_of_days, deltaes.copy())
        answer2 = slow_main(number_of_fogs, heights.copy(), number_of_days, deltaes.copy())
        for i in range(len(answer1)):
            if answer2[i] != answer1[i]:
                print(f"number_of_fogs = {number_of_fogs}")
                print(f'heightes = {heights}')
                print(f'number_of_days = {number_of_days}')
                print(f'deltaes = {deltaes}')
                print(f'correct_answer = {answer2}')
                print(f'my_answer = {answer1}')
                print(_)
                exit(-1)

test()

"""
[-5, -13, -11, 2, 13, -10, 16, -10, 3, 14] [-14, 10, -9, 2, -12]
number_of_fogs = 10
heightes = [-5 -13 -11 2 13 -10 16 -10 3 14]
number_of_days = 5
deltaes = [-14 10 -9 2 -12]
correct_answer = [(2, 143), (31, 72), (4, 135), (10, 121), (0, 231)]
my_answer = [(-13, 128), (22, 63), (-32, 99), (-44, 107), (-84, 187)]
0
"""

"""
10
-5 -13 -11 2 13 -10 16 -10 3 14
5
-14 10 -9 2 -12
"""