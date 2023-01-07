from itertools import permutations


words = set()
for word in permutations('ТРАТАТА'):
    word_str = ''.join(word)
    words.add(word_str)

print(words)
print(len(words))