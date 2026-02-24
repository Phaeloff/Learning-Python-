# %%
import pandas as pd

idades =[ 23, 34, 52, 61, 77, 21, 67, 71, 72, 75]

nomes = [
    "TÉO", "MARIA", "LUIZ", "ANA", "NAH",
    "DANI", "FER", "MAH", "TITO", "RAFA"
]

series_idades = pd.Series(idades)
series_nomes = pd.Series(nomes)

# %%

df = pd.DataFrame()
df["idades"] = series_idades
df["nomes"] = series_nomes

# %% - retorna uma séria onde indice retorna mesmo indice do dataframe
df["idades"]

# %% - acesse uma linha especifica do dataframe desejada

df.iloc[0]

# %% - saber o primeiro nome do dataframe

df.iloc[0]["nomes"]

# %% - idade da ultima pessoa

df.iloc[-1]["idades"]