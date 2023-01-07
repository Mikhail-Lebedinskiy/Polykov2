answer = 0
for i in range(-10000, 10000):
    n = 1
    s = i
    while s > n:
        s = s - 15
        n = n * 5
    if n == 125:
        answer += 1
        print(i)
print(answer)