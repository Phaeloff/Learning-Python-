# %%
import pandas as pd
df = pd.read_csv("../data/clientes.csv")
df

#%%
df.shape

#%%
df.info(memory_usage='deep')

#%%

df.dtypes

#%%
df[["idCliente"]]

#%% - selected idCliente, qtPontos From df Limit 5

df[["idCliente", "qtPontos"]].tail(5)

#%% - select idCliente, IdTransacao, qtPontos
#From of
#Limit 5

df[["idCliente", "idTransacao", "qtPontos"]]


#%%

colunas =  list(df.columns)
colunas.sort()
colunas

df = df[colunas]
df