# %%

import pandas as pd

df = pd.read_csv("../data/clientes.csv")

df = pd.concat(['idCliente', 'Transacoes'])

df