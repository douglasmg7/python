#!/usr/bin/env python3
import ticks_keywords

#  print(tick_b3sa)
#  print(ticks_keywords.tick_b3sa)
#  print(type(ticks_keywords.tick_b3sa['Bolsa']))
#  print(ticks_keywords.tick_b3sa['Bolsa'].search('É uma Bolsa de valores'))

for k, v in ticks_keywords.tick_b3sa.items():
    print(f'{k}: {v.search("É uma Bolsa de valores")}')
    #  print(v)
#  #  r = ticks_keywords.tick_b3sa['Bolsa']
