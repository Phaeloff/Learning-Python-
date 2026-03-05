# %%

import pandas as pd

# %%

df = pd.DataFrame({
    "nome": ['teo', 'lara', 'nah', 'bia', 'mah', 'lara', 'mah'],
    "sobrenome": ['calvo', 'calvo', 'ataide', 'ataide', 'silva', 'silva', 'silva'],
})

df
# %% - tirar as linhas repetidas.

df.drop_duplicates(keep='last')
df

# %% - pegar o nome e sobrenome para retirar linhas repetidas
df.drop_duplicates(subset=["nome", "sobrenome"])
df

