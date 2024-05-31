#!/usr/bin/env python3

# Same result.
s = 'sda' + 'df'
print(s)
s = 'sda' 'df'
print(s)
s = ('sda'
     'df')
print(s)

# Strins can be indexed.
s = 'python'
print(s[0])
print(s[0:3])