# No need for index.
l = list(range(5))
for item in l:
    print(item)

l = ['a', 
    'b', 
    'c',
    ]

# Need the index.
for i, item in enumerate(l):
    print(i, item)

# Emulate for as used in c.
for i in range(0, 5, 1):
    print(i)