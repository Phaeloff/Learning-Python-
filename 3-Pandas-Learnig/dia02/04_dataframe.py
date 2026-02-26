#%%

import pandas as pd

df_clientes = pd.read_csv("../data/clientes.csv")

df_clientes


#%% - como retornar quantidade de linha.

df_clientes.head(n=10)

# %% - retornar as ultimas linhas do dataset.

df_clientes.tail()

# %% - sortido os numeros, pega numero aleatorios.

df_clientes.sample(10)

# %% - mostrar quantidade de linha e colunas.

df_clientes.shape

# %% - descobrir os nomes das colunas existentes

df_clientes.columns

# %% - indices do dataframe

df_clientes.index

# %% - tipos de coluna e informações

df_clientes.info()

# %% - informa uma série onde os valores dentros os valores dentro dessee é um valor de cada coluna.

df_clientes.dtypes

