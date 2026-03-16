# %%

import pandas as pd

df = pd.read_csv("homicidios_consolidado.csv" , sep=";")

df.head()

# %%
df_stack = (df.set_index(["nome", "período"])
            .stack())
df_stack = df_stack.reset_index()
df_stack.columns = ["Nome", "Período", "metrica", "valor"]
df_stack
# %% - unstack desempilhar

(df_stack.set_index(["Nome", "período", "metrica"])
            .unstack()
            .reset_index()
)