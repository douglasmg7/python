#!/usr/bin/python3

#  file_to_write = open('a.txt', 'a')
#  print('New line', file=file_to_write)
#  file_to_write.close()

# Append to file.
with open('a.txt', 'a') as file:
    print('New line x', file=file)