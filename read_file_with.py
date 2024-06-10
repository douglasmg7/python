#!/usr/bin/python3

with open('a.txt', 'r') as file:
    contents = file.read()
    print(type(contents))
    print(contents)

with open('a.txt', 'r') as file:
    contents = file.readlines()
    print(type(contents))
for line in contents:
    print(type(line))
    print(line)

#  with open('a.txt', 'r') as file:
  #  for line in file:
    #  print(line)
