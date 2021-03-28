#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):

    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        print('foo() called')
    def bar(self):
        print('bar() called')

# b = Base()    # Will raise a error

assert issubclass(Concrete, Base)

c = Concrete()
c.foo()

