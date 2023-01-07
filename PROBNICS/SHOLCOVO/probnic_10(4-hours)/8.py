from itertools import permutations


answer = set()
for word in permutations('ПРОКРАСТИНАЦИЯ', 4):
    word_str = ''.join(word)
    if word_str[0] not in 'ОАИЯ':
        continue
    if word_str[-1] not in 'ОАИЯ':
        continue
    if 'АР' not in word_str:
        continue
    if 'АС' in word_str:
        continue
    answer.add(word_str)

print(sorted(list(answer)))
print(answer)
print(len(answer))
