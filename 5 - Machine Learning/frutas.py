# %%

import pandas as pd

df = pd.read_excel("data/dados_frutas.xlsx")

df

# %%

from sklearn import tree

arvore = tree.DecisionTreeClassifier()

# %%

y = df['Fruta']
caracteristicas = ['Arredondada', 'Suculenta', 'Vermelha']
x = df[caracteristicas]

# %%
# isso aquii é machine learning, o algoritmo vai aprender a classificar as frutas a partir dos dados que passamos para ele
arvore.fit(x, y)

# %%
# vamos testar o modelo com uma fruta que é arredondada, suculenta e vermemelha.

arvore.predict([[0, 1, 1]])

# %%

import matplotlib.pyplot as plt

plt.figure(dpi=400)

tree.plot_tree(arvore,
                feature_names=caracteristicas,
                class_names=arvore.classes_,
                filled=True)