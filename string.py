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
s2 = s[0:3]
print('s2: ', s2)
s = '111111111111'
print('s1: ', s)
print('s2: ', s2)

# String to list -> list to string.
s='olá mundo'
l=list(s)
print('l:', l)
l[0] = 'O'
print('l:', l)
s=''.join(l) + '!'
print('s: ', s)

# Find.
print(s.find('mu'))

# Replace:
print(s.replace('mundo', 'world'))

# Split:
print('split: ', s.split(' '))

print('isalpha: ', s.isalpha())
print('isdigit: ', s.isdigit())

# Upper case:
print('upper: ', s.upper())

# Format:
s = '%s e %s' % ('plantas', 'formigas')
print(s)

s = '{} e {}'.format('plantas', 'formigas')
print(s)
