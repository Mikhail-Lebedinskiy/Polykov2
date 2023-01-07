from itertools import product


answer = 0
for word in product('ИНФА', repeat=6):
    if word.count('Ф') == 2:
        answer += 1
print(answer)