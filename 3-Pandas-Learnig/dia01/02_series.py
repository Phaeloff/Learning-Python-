# %%
import pandas as pd

idade =[ 23, 34, 52, 61, 77, 67, 71, 72, 75]

media = sum(idade) / len(idade)
print("Media:", media)

diffs = 0
for i in idade:
    diffs += (1 - media) ** 2

variancia = diffs / (len(idade)-1)

print("Variância:", variancia)

# %%
import pandas as pd

# Lista vazia - pd.Series igual As Lista acima.
series_idades = pd.Series(idade)
series_idades

# %% - Metodos de Séries

media = series_idades.mean()

variancia = series_idades.var()

summary_idades = series_idades.describe()

summary_idades

