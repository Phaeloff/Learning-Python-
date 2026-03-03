# %%

import pandas as pd
import numpy as np


df = pd.read_csv("../data/clientes.csv")

df.head()

# %%

df["pontos_100"] = df["qtdePontos"] + 100

# %%

df.head()

# %% - Operação entre duas séries - tem twitch ou e-mail

df["emailTwitch"] = df["flEmail"] + df["flTwitch"]

# caso deseja se ambos tem conta.
df["emailTwitchambos"] = df["flEmail"] * df["flTwitch"]

# quantas redes sociais tem cadastradas

df["QuantidadedeRedesSociais"] = df["flEmail"] + df["flTwitch"] + df["flYoutube"] + df["flBlueSky"] + df["flInstagram"]

#%% - ao menos uma rede social

df["ApenasumaRedesSociais"] = df["flEmail"] * df["flTwitch"] * df["flYoutube"] * df["flBlueSky"] * df["flInstagram"]

# %% -

df["qtdePontos"].describre()

# %%

df["logPontos"] = np.log(df["qtdePontos"]+1 )
df["logPontos"].describe()

