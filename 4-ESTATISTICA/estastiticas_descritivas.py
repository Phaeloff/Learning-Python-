# %%
import pandas as pd
df = pd.read_csv("data1/points_tmw.csv")
df.head()

# - Media
media = df["qtdPontos"].mean()
print("Média:", media)

# -minimo
min = df["qtdPontos"].min()
print("Minimo:", min)

#Quartil
quartil_1 = df["qtdPontos"].quantile(0.25)
print("Primeiro Quartil:", quartil_1)

# - Mediana
Mediana = df["qtdPontos"].median()
print("Mediana:", Mediana)

# - Terceiro quartil 3/4
quartil_3 = df["qtdPontos"].quantile(0.75)
print("Terceiro Quartil", quartil_3)

# - Maximo
Maximo = df["qtdPontos"].max()
print("Maximo:", Maximo)

# %% - forma reduzida.
df.describe()
