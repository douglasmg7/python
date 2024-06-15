#!/usr/bin/python
i=0
b='1101'

while b!= '':
    i = i * 2 + ord(b[0]) - ord('0')
    b = b[1:]
    print(f'i: {i}, b: {b}')
