#!/usr/bin/env python
import json
m = {'a': 23, 'b': 42, 'c': 0xc0ffee}
print(m)

s = json.dumps(m, indent=4, sort_keys=True)
print(type(s))
print(s)

# load string
m2 = json.loads(s)
print(type(m2))
print(m2)