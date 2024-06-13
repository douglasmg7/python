#!/usr/bin/python
print([x ** 2 for x in range(3,9)])
print([x ** 2 for x in range(1,15) if x % 2 == 0])
print({x: x ** 3 for x in [1, 2, 3, 4 ,5]})
even_numbers = [x for x in range(0, 40) if x % 2 == 0]
print('Even numbers: ', even_numbers)
print('Zero numbers: ', [0 for _ in even_numbers])

matrix = [(x, y) 
          for x in range(10) 
          for y in range(x+1,10)]
print(f'Matrix: {matrix}')