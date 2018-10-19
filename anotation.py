#!/usr/bin/python3

# A function using anotation and docstring.
# Anotation is not used by compile, it is just from programming reference.
# help() use anotation and docstring for print information about de function.
def print_some_thing(word:str) -> set:
    """" Print each char from received word """
    s = set(word)
    for ch in s:
        print(ch)
    return s

print_some_thing('asdf')

