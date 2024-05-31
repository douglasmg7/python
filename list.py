states = ['mg', 'rj', 'sp', 'rs', 'pr']
print(states)
print('First', states[0])
print('Last', states[-1])

# Print all states.
for state in states:
    print(state)

st = states
states.append('pa')
print(states)
print(st)

# Point to same reference.
print(id(states))
print(id(st))

# Remove some itens.
states[2:4] = []
print(states)