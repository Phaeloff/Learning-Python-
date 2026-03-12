# %%

import pandas as pd
import sqlalchemy

from sklearn import cluster

with open ("etl.sql") as open_file:
    query = open_file.read()

print(query)

# %% - Fazer a Query do SQL
engine= sqlalchemy.create_engine("sqlite:///../data/olist.db")


df = pd.read_sql_query(query, con=engine)

df


# %% - Criar uma tabela.

kmean = cluster.KMeans(n_clusters=4)
kmean.fit(df[['totalRevenue', 'qtSalles']])

df["cluster"] = kmean.labels_
df

# %% - Encaminhar a tratativa de volta para o SQL.

df.to_sql('sellers_cluster', con=engine, index=False)