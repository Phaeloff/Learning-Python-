# %%

import pandas as pd

transacoes = pd.read_csv("../data/transacoes.csv")

transacoes.head()

# %%
clientes = pd.read_csv("../data/clientes.csv")

clientes.head

# %% - só pega caso tenha nas duas tabelas - suffixes(renomeia lista repetida)

transacoes.merge(
                right= clientes,
                how='left',
                on=['idCliente'],
                suffixes=["Transacao", "Cliente"],
)

# %%

produtos = produtos[produtos["descProduto"]=="Presença Streak"]

(transacoes.merge(transacao_produto, on ="idTransacao", how="left")
            .merge(produtos, on=["idProduto"], how="inner")
            .groupby(by="idCliente")["idTransacao"]
            .count()
            .sort_values(ascending=False)
            .head(1)
)