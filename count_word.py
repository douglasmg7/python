#!/usr/bin/python
from collections import Counter

with open('./sometext') as file:
    content = file.read().split()
    #  [print(content[i]) for i in range(1,100)]
    #  print(content)
    c = Counter(content)
    for word, count in c.most_common(20):
        print(f'{word}: {count}')
