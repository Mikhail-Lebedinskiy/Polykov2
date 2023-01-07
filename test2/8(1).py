from itertools import product


words = [''.join(i) for i in product('ПАРУС', repeat=5)]
words.sort()
for i, word in enumerate(words):
    if word[0] == 'У' and 'АА' not in word:
        print(i + 1)
        break