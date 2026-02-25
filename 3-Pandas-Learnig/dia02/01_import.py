# %% - carregar o dado
import pandas as pd


df = pd.read_csv("../data/clientes.csv")
df

#%% - Salvar o arquivo - CSV

df.to_csv("clientes.csv", index = False)

# %% - salvar em parquet

df.to_parquet("clientes.parquet", index = False)

#%% - Salvar um excel

df.to_excel("clientes.xlsx", index = False)

# %% - Ler o Excel

df_3 = pd.read_excel("clientes.xlsx")
df_3