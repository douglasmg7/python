#!/usr/bin/python
s=sorted([4, 1, 5, -3, -1])
print(f's original: {s}')

s=sorted([4, 1, 5, -3, -1], reverse=True)
print(f's sorted: {s}')

s=sorted([4, 1, 5, -3, -1], key=abs)
print(f's sorted using abs: {s}')

s=sorted([4, 1, 5, -3, -1], key=abs, reverse=True)
print(f's sorted using abs and reverse: {s}')