# %%

import pandas as pd

df = pd.read_csv('../data/transacoes.csv')

df.head()

# %%

pontos = [10, 1, 1, 1, 50, 100, 130, 30 ,25, 50]
filtro = []

valores_50_mais = []

for i in pontos:
    filtro.append(i>=50)

resultado = []
for i in range(len(pontos)):
    if filtro[i]:
        resultado.append(pontos[i])

resultado

# %%

brinquedo = pd.DataFrame (
    {
        "nome": ["theo", "nah", "mah"],
        "idade": [ 10, 52, 41 ],
        "uf": ["sp", "rj", "pr"],
    }
)

filtro = brinquedo["idade"] >= 18

brinquedo[filtro]


# %%
import pandas as pd

df = pd.read_csv('../data/transacoes.csv')

df.head()

# %%

filtro = df["QtdePontos"] >= 50
df[filtro]

# %% - entre 50 e 100

filtro = (  df["QtdePontos"] >=50  & df["QtdePontos"] <100)
filtro

# %% ou é 50 ou 100

filtro = (  df["QtdePontos"] == 50 | df["QtdePontos"] == 100)
filtro

# %% - combinar dois valores - pontos entre 0 e 50 ou do ano de 2025 para frente

filtro = (  df["QtdePontos"] > 0 & (df["QtdePontos"] <= 100) | (df["DtCriacao"] >= '2025-01-01'))
filtro