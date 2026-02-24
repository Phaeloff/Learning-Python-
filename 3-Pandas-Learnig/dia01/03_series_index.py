# %%
import pandas as pd

idade =[ 23, 34, 52, 61, 77, 21, 67, 71, 72, 75]

# Lista vazia - pd.Series igual As Lista acima.
series_idades = pd.Series(idade)
series_idades

# %%

idade[0]
series_idades[0]
# %%

series_idades = series_idades.sort_values()
series_idades

# %%

series_idades[0]

# %% - iloc

series_idades.iloc[0]

# %% - iloc

series_idades.iloc[:3]

# %% 
idade =[ 23, 34, 52, 61, 77, 21, 67, 71, 72, 75]

indexs = [
    "TÉO", "MARIA", "LUIZ", "ANA", "NAH",
    "DANI", "FER", "MAH", "TITO", "RAFA"
]
series_idades = pd.Series(idade, index=indexs)
series_idades

# %%
series_idades.iloc[0]
