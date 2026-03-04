# %%

import pandas as pd

# %%

df = pd.read_csv("../data/clientes.csv")

df

# %% - inteiro

df["qtdePontos"].astype(int)

#%% - float

df["qtdePontos"].astype(float)

# %% - string
df["qtdePontos"].astype(str)

# %% - converter data
replace = {
    "0000-00-00 00:00:00.000": "2024-02-01 09:00:00.000",
    "NaN" : "2024-02-01 09:00:00.000"
    }

df["dtCriacao"] = pd.to_datetime(df["dtCriacao"].replace{replace})
# %%

df["dtCriacao"].dt.year()



