from itertools import product


answer = set()
for p in product("POLYGON", repeat=5):
    word = ''.join(p)
    if word == word[::-1] and word[2] in ['O', 'Y']:
        answer.add(word)
print(answer)
print(len(answer))