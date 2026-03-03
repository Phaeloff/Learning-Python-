# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")

clientes.head()

filtros = clientes["QtdePontos"] == 0
clientes_0 = clientes [filtros]
clientes_0["flag_1"] = 1

# %%

clientes_0