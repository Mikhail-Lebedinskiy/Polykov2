
def f(i):
    answer = ""
    while i != 0:
        answer += str(i % 4)
        i = i // 4
    return answer[::-1]
q = 0
for i in range(10000):
    if len(f(i)) == 4 and int(f(i), 8) % 4 == 0:
        q += 1
print(q)