class CountFromBy:
  def __init__(self, v: int=0, i: int=1) -> None:
    self.val = v
    self.incr = i

  def increase(self) -> None:
    self.val += self.incr

  def __repr__(self) -> str:
    return str(self.val)

print('CountFromBy imported.')

# Create a object.
obj = CountFromBy(3, 10)
print('val: ', obj.val)
print('incr: ', obj.incr)
obj.increase()
print('val after increase: ', obj.val)
print('obj type: ', type(obj))
print('obj id: ', id(obj))
print('obj id in hex: ', hex(id(obj)))
print('Using __repr__', obj)
