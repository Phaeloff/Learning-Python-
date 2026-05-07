#%%

import pandas as pd

df = pd.read_excel("data/dados_cerveja_nota.xlsx")

df.head()

x = df[['cerveja']] #isso é uma mastrix (dataframe)
y = df[['nota']] #isso é um valor (séris)

#isso é o aprendizado de máquina.
reg = liner_model.LinearRegression()
reg.fit(x,y)

# %%

a, b = reg.intercept_, reg.coef[0]
print(a,b)

# %%

predict = reg.predict(x.drop_duplicates())

# %%
import matplotlib as plt

plt.plot(x['cerveja'], y, 'o')
plt.grid(True)
plt.title("Relação Cerveja vs Nota")
plt.xlabel("Cerveja")
plt.ylabel("Nota")

plt.plot(x.drop_duplicates()['cerveja'], predict)

