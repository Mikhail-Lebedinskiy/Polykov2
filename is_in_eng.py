import enchant
from itertools import product


d = enchant.Dict("en_US")

s = 'grayn'

for word in set(product(s, repeat=len(s))):
    if d.check(''.join(word)):
        print(''.join(word))
"""broker = enchant.Broker()
broker.describe()
broker.list_languages()"""