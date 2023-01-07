# arr = [3, 4]
#
# print(f'x_0 = {arr[0]}')
# print(f'x_1 = {arr[1]}')
#
# for i in range(2, 20):
#     arr.append(arr[i - 2] ** 2 - (i - 1) * arr[i - 1])
#     print(f'x_{i} = {arr[i]}')


arr = [4, 1 / 4]

print(f'x_0 = {arr[0]}')
print(f'x_1 = {arr[1]}')


for i in range(2, 30):
    arr.append(0.5 * (arr[i - 2] + 1 / arr[i - 1]))
    print(f'x_{i} = {arr[i]}')