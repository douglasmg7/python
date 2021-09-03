import re

# B3
#  print('ticks')
tick_b3sa = {
    'investimento': re.compile(r'\binvestimento\b', flags=re.IGNORECASE),
    'Bolsa': re.compile(r'\bBolsa\b'),
}
#  print(tick_b3sa)