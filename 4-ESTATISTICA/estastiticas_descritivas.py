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

# - variancia
variancia = df["qtdPontos"].var()
print("Variância:", variancia)

# - desvio padrão
desvio_padrao = df["qtdPontos"].std()
print("Desvio Padrão", desvio_padrao)

# - amplitude
amplitude = df['qtdPontos'].max() - df["qtdPontos"].min()
print("Amplitude:", amplitude)

df.describe()
# %% - forma reduzida.

print("\n\n############\n")
print("Estatisticas de Posição para usuários:\n")

usuarios = (df.groupby(["idUsuario"])
                .agg({
            "idTransacao":"count",
            "qtdPontos": "sum",
                }).reset_index()
            )
# %%

summario = usuarios[['idTransacao', 'qtdPontos']].describe()
print(summario.to_string())
