#!/usr/bin/python3

file_to_write = open('a.txt', 'a')
print('New line', file=file_to_write)
file_to_write.close()