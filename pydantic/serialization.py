#!/home/dmg/miniconda3/envs/pydantic/bin/python

from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

douglas = Person(first_name='Douglas', last_name='Gomes', age=48)
newton = Person(first_name='Isac', last_name='Newton', age=84)

print(f'dic: {newton.__dict__}, type: {type(newton.__dict__)}')
print(f'dic: {newton.model_dump()}, type: {type(newton.model_dump())}')
print(f'json: {newton.model_dump_json()}, type: {type(newton.model_dump_json())}')

n = newton.model_dump_json(indent=2, exclude=['last_name'])
print(n)

n = newton.model_dump_json(indent=2, include=['age'])
print(n)