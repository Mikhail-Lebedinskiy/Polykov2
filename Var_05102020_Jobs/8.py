from itertools import permutations


good_words = set()
for word in permutations('запись'):
    word_str = ''.join(word)
    index = word_str.find('ь')
    if index == 0:
        continue
    if word_str[index - 1] in 'аи':
        continue
    good_words.add(word_str)


print(len(good_words))
print(good_words)