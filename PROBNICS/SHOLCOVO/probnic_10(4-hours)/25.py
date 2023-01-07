
answer = 0
for k in range(1, 25, 2):
    if not(33_333_333 <= 2 * k ** 6 <= 99_999_999):
        continue
    answer += 1
    print(2 * k ** 6)

