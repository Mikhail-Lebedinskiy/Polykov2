def f(i):
    answer = ""
    while i != 0:
        answer += str(i % 8)
        i = i // 8
    return answer[::-1]

i = 7 * (512**1912) + 6 * (64**1994) - 5 * (8**1991) - 4 * (8**1960) - 2022
a = f(i).count("7")
print(a)