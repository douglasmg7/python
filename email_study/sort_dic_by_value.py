#!/usr/bin/env python3

xs = {'a': 4, 'b':3, 'c':2, 'd':1} 

result = sorted(xs.items(), key=lambda x: x[1])
print(result)

import operator
result = sorted(xs.items(), key=operator.itemgetter(1))
print(result)

