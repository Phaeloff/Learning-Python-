# %%

import pandas as pd

url = "https://pt.wikipedia.org/wiki/Rio_de_Janeiro_(estado)"

dfs = pd.read_html(url)

uf = dfs[1]

# %%

uf.dtypes