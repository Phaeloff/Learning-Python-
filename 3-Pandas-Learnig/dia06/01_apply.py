# %%
import pandas as pd

df = pd.read_csv("../data/clientes.csv")

df.head()

idCliente = "000ff655-fa9f-4baa-a108-47f58ec52a1"

def get_last_id(x):
    return x.split("-")[-1]

# %%

get_last_id("000ff655-fa9f-4baa-a108-47f58ec52a1")

# %%

id_novo = []

for i in df["idCliente"]:
    novo = get_last_id(i)
    id_novo.append(novo)

df["novo_id"] = id_novo

df.head()

# %%

df["idCliente"].apply(get_last_id)