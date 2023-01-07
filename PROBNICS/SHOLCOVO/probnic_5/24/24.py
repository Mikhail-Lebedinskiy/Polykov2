with open('24__x9cg.txt') as file:
    s = file.read().strip()
s += 'Z'
answer = 0
last_Z_cord = -1

for i in range(len(s)):
    if s[i] == 'Z':
        answer = max(answer, i - last_Z_cord - 1)
        last_Z_cord = i
print(answer)