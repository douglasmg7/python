#!/home/douglasmg7/miniconda3/envs/web_scraping/bin/python3
import pandas as pd

states = ['California', 'Texas', 'Florida', 'New York']
population = [100, 200, 300, 400]
dic_states = {'states': states, 'population': population}

df_states = pd.DataFrame.from_dict(dic_states)
df_states.to_csv('states_population.csv', index=False)