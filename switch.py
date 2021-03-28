#!/usr/bin/env python3

def dispatch_dic(operator, x, y):
    return {
        'add': lambda: x + y,
        'sub': lambda: x - y,
        'mul': lambda: x * y,
        'sub': lambda: x / y,
        }.get(operator, lambda: none)()

print(dispatch_dic('mul', 2, 3))
