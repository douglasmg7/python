#!/usr/bin/python3

def change(val): 
    val = 4
    print('inside func: ', val)
    return val

temp = 0
print('before func: ', temp)

change(temp)
print('after func: ', temp)
