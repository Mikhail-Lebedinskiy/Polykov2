def f(x, y):
    x = str(x)
    y = str(y)
    a = x[-1] == '6'
    b = y[-1] == '6'
    if (a or b) and (a != b):
        return True
    return False


with open('17.txt') as file:
    data = []
    for line in file:
        data.append(int(line.strip()))

minn = 10 ** 9
for num in data:
    if str(num)[-1] != '6':
        continue
    if num < minn:
        minn = num
print(minn ** 2)
answer = []
for i in range(1, len(data)):
    if f(data[i], data[i - 1]):
        if data[i] ** 2 + data[i - 1] ** 2 < minn ** 2:
            answer.append(data[i] ** 2 + data[i - 1] ** 2)
print(len(answer))
print(max(answer))

