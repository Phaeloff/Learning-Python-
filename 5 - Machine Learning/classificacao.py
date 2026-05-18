# %%
import pandas as pd
import matplotlib.pyploty as plt

df = pd.read_excel("data/dados_cerveja_nota.xlsx")

df

df['aprovado'] = (df['nota'] > 5).astype(int)
df

# %%

plt.plot(df['cerveja'], df['aprovado'], 'o', color='royalblue')
plt.grid(true)
plt.title("Cerveja vs Aprovação")
plt.xlabel("Cervejas")
plt.ylabel("Aprovado")

# %%

from sklearn import linear_model

reg = linear_model.LogisticRegression(penalty=None, fit_intercept=True)

reg.fit(df(['cerveja']), df['aprovado'])

reg_predict = reg.predict(df[['cerveja']].drop_duplicates())
reg_prob = reg.predict(df[['cerveja']].drop_duplicates())[:,1]

plt.figure(dpi=400)
plt.plot(df['cerveja'], df['aprovado'], 'o', color='royalblue')
plt.grid(true)
plt.title("Cerveja vs Aprovação")
plt.xlabel("Cervejas")
plt.ylabel("Aprovado")

plt.plot(df['cerveja'].drop_duplicates(),reg_predict, color='tomato')
plt.plot(df['cerveja'].drop_duplicates(),reg_prob, color='red')