#!/usr/bin/env python3

# Namedtuples are immutable containers, just like regular tuples
# All attributes on a namedtuple object follow the “write once, read many” principle
# A good way to view them is to think that namedtuples are a memoryeсcient shortcut to deпning an immutable class in Python manually

from collections import namedtuple

Car = namedtuple('Car', 'color milage')

chevette = Car('blue', 123)

print(chevette)
print(chevette.color)
print(chevette[0])
# chevette.color = 'green'  # Error

# Create a tuple
print(tuple(chevette))

# Unpack
color, milage = chevette
print(f'color: {color}, milage: {milage}')
# Unpack again
print(*chevette)

# You can extend a namedtuple’s class like any other class and add methods and new properties to it that way
class MyCarWithMethods(Car):
    def hexcolor(self):
        if self.color == 'red':
            return '#ff0000'
        else:
            return '#000000'

monza = MyCarWithMethods('blue', 345)
print(monza.hexcolor())

# The easiest way to create hierarchies of namedtuples is to use the base tuple’s _fields property
ElectricCar = namedtuple('ElectricCar', Car._fields + ('charge',))
print(ElectricCar('white', 123, .5))

# As a ordered dic
my_car = ElectricCar('white', 123, .5)
print(my_car._asdict())

# Shallow copy
print(my_car._replace(color='blue'))

# Create new instances of a namedtuple from a sequence or iterable
print(Car._make(['blue', 987]))
