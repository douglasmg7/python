#!/home/dmg/miniconda3/envs/pydantic/bin/python

from pydantic import BaseModel, ValidationError

class Person(BaseModel):
    first_name: str
    last_name: str
    age: int

p = Person(first_name='Douglas', last_name='Gomes', age=48)
print(f'p: {p}')

p_dic = {
    'first_name': 'Isac',
    'last_name': 'Newton',
    'age': 84
}
# Avoid this away.
p = Person(**p_dic)
print(f'p: {p}')

# Bether away.
p = Person.model_validate(p_dic)
print(f'p: {p}')

# Missing data.
p_dic = {
    'first_name': 'Isac',
}
try:
    p = Person.model_validate(p_dic)
    print(f'p_dic {p}')
except ValidationError as err:
    print(err)

# Using json.
p_json = '''
{
    "first_name": "Isac",
    "last_name": "Newton",
    "age": 84
}
'''
p = Person.model_validate_json(p_json)
print(f'p_json: {p}')