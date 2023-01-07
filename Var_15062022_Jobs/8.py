from itertools import product

letters = sorted(list('ПЯТЬДНЕЙ'))

answer = -1
for i, word in enumerate(product(letters, repeat=4)):
    word_str = ''.join(word)
    if 'Я' not in word_str and 'Е' not in word_str and len(word_str) == len(set(word_str)):
        answer = i
print(answer)

