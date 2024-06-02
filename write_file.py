#!/usr/bin/python3

#  file_to_write = open('a.txt', 'a')
#  print('New line', file=file_to_write)
#  file_to_write.close()

# Append to file.
with open('write_file.txt', 'w') as file:
    print('new file', file=file)