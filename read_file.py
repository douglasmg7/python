#!/usr/bin/python3

# 'r' Open file for read.
# 'w' Open file for write. If the file alredy contains data, empty the file first. 
# 'a' Open file for appending.
# 'x' Open a new file for writing. Fail if the file alredy exists.

file = open('a.txt') # Or file = open('a.txt', 'r')

for line in file:
  print(line)
file.close()