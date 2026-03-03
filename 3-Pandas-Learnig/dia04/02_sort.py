# %%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv")

clientes

max_pontos = clientes["qtdePontos"].max()
filtro = [clientes["qtdePontos"] == max_pontos]
clientes = [filtro]

# %% - forma descrecente

clientes.sort_values(by="qtdePontos", ascending=False)

# %% - forma crescente

clientes.sort_values(by="qtdePontos")

# %% - pegar os 5 primeiros com mais pontos

top_5 = (clientes.sort_values(by="qtdePontos", ascending=False)
        .head(5)["idCliente"])

# %%
clientes

# %% -

brinquedo = pd.DataFrame(

    {
        "nome": ["teo", "luiz", "flavio", "joao"],
        "idade": [ 21, 45, 42, 21],
        "salario": [ 2141, 5233, 4214, 5233],
    }
)

brinquedo

# %%

brinquedo.sort_values(by=["salario", "idade"], ascending=[False, True])

