#!/usr/bin/python3

# A function using anotation and docstring.
# Anotation is not used by compile, it is just from programming reference.
# help() use anotation and docstring for print information about de function.
def print_some_thing(word:str, sep:str='-') -> set:
  """" Print each char from received word """
  s = set(word)
  for ch in s:
    print(ch)
    print(sep)
  return s

# Call using positional argument.
print_some_thing('asdf')
  
# Call using argument name.
print_some_thing(sep='_', word='asdf')
