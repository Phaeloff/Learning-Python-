#%%
import pandas as pd
import sqlalchemy

df = pd.read_csv("data1/points_tmw.csv")

df.head()

engine = sqlalchemy.create_engine("sqlite:////data/tmw.db")

df.to_sql("points", engine, if_exists="replace", index=False)

# %% - criando uma série refere tabela de frequencia.

#cada produto
freq_produto = (df.groupby(["descProduto"])[["idTransacao"]]
            .count())

#frequencia acumulada .cumsum
freq_produto["Freq. Abus Acum."] = freq_produto["idTransacao"].cumsum()

#frequencia absoluta / total da quantidade
freq_produto["Freq. Rel."] = freq_produto["idTransacao"] / freq_produto["idTransacao"].sum()

#frequencia relativa
freq_produto["Frq. Rel. Acum"]= freq_produto["Freq. Rel."].cumsum()

freq_produto

# %%
freq_cat = (df.groupby(["descCategoriaProduto"])[["idTransacao"]]
                .count()
                .rename(columns={"idTransacao": "Freq. Abs."})
                )

freq_cat["Freq.Abs. Acum."] = freq_cat["Freq. Abs."].cumsum()

freq_cat["Freq. Rel."] = freq_cat["Freq. Abs."]/ freq_cat["Freq. Abs."].sum()

freq_cat["Freq.Abs. Acum."] = freq_cat["Freq. Rel."].cumsum()

freq_cat
