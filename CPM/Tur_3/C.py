def split_list(arr):
    return [], []


count_of_food, all_time = [int(i) for i in input().split()]

foods = []

for i in range(count_of_food):
    foods.append((int(j) for j in input().split()))

foods = sorted(foods, key=lambda x: x[0])

foods_left, foods_right = split_list(foods)





