# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv")

df

# %% - ignorando os NaN - Caso tenha alguma linha com NaN é retirado da série

df.dropna()

# %% - com o "how" a linha inteira tem quer ser NaN

df.dropna(how="all")

# %% - nesses casos apenas onde idade está sendo NaN

df = pd.DataFrame({
    "nome": ["téo", None, "Nah", "Marcio"],
    "idade": [None, None, 42, 54],
    "salario":[321321, 2312321, None, 2121],

})

df.dropna(how="all", subset=["idade"])

#  - caso seja as duas
df.dropna(how="all", subset=["idade", "nome"])

# - caso seja apenas uma

df.dropna(how="any", subset=["idade", "salario"])

# %% - Fill "NaN" preencher os valores vazios

df['idade'].fillna(0)
df["nome"].fillna("Sem nome")

# colocar como todos NaN da lista seja apenas uma coisa

df.fillna(0)
